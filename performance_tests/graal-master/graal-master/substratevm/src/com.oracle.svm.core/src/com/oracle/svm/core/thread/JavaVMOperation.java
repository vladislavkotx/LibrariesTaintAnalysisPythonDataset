/*
 * Copyright (c) 2015, 2019, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.  Oracle designates this
 * particular file as subject to the "Classpath" exception as provided
 * by Oracle in the LICENSE file that accompanied this code.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */
package com.oracle.svm.core.thread;

import jdk.graal.compiler.word.Word;
import org.graalvm.nativeimage.CurrentIsolate;
import org.graalvm.nativeimage.IsolateThread;

import com.oracle.svm.core.SubstrateOptions.ConcealedOptions;
import com.oracle.svm.core.SubstrateUtil;
import com.oracle.svm.core.Uninterruptible;
import com.oracle.svm.core.heap.RestrictHeapAccess;
import com.oracle.svm.core.heap.VMOperationInfo;
import com.oracle.svm.core.jdk.SplittableRandomAccessors;
import com.oracle.svm.core.util.VMError;

/**
 * The abstract base class for all VM operations that are allocated on the Java heap. Allocating the
 * VM operation on the Java heap is preferable but not always possible (see
 * {@link NativeVMOperation}). {@link JavaVMOperation} objects should be short lived and only
 * enqueued/executed once. For increased thread safety, it is prohibited to allocate
 * {@link JavaVMOperation}s that live in the image heap (see note below).
 * <p>
 * Note: the VM operation infrastructure supports that {@link JavaVMOperation}s are reused and
 * executed multiple times. However, extra care must be taken as each VM operation object can only
 * be in the VM operation queue once. Therefore, it must be guaranteed that the VM operation is
 * executed before it is enqueued again. Otherwise, this could result in various race conditions,
 * especially if {@linkplain ConcealedOptions#UseDedicatedVMOperationThread} is enabled.
 */
public abstract class JavaVMOperation extends VMOperation implements VMOperationControl.JavaAllocationFreeQueue.Element<JavaVMOperation> {
    protected IsolateThread queuingThread;
    private long queuingThreadId;
    private JavaVMOperation next;
    private volatile boolean finished;

    protected JavaVMOperation(VMOperationInfo info) {
        super(info);
        /*
         * Calling SplittableRandomAccessors#getDefaultGen() here to prevent
         * SplittableRandomAccessors#initialize synchronized method call inside VMOperation lock,
         * that can leads to deadlock.
         */
        SplittableRandomAccessors.getDefaultGen();
        VMError.guarantee(!SubstrateUtil.HOSTED, "must not be created at image build time");
    }

    @Override
    public JavaVMOperation getNext() {
        return next;
    }

    @Override
    public void setNext(JavaVMOperation value) {
        next = value;
    }

    public void enqueue() {
        VMOperationControl.get().enqueue(this);
    }

    @Override
    protected IsolateThread getQueuingThread(NativeVMOperationData data) {
        return queuingThread;
    }

    @Override
    protected long getQueuingThreadId(NativeVMOperationData data) {
        return queuingThreadId;
    }

    @Override
    protected boolean isFinished(NativeVMOperationData data) {
        return finished;
    }

    @Override
    @Uninterruptible(reason = "Called from uninterruptible code.", mayBeInlined = true)
    protected void markAsQueued(NativeVMOperationData data) {
        finished = false;
        queuingThread = CurrentIsolate.getCurrentThread();
        queuingThreadId = JavaThreads.getCurrentThreadIdOrZero();
    }

    @Override
    protected void markAsFinished(NativeVMOperationData data) {
        queuingThread = Word.nullPointer();
        queuingThreadId = 0;
        finished = true;
    }

    @Override
    protected final boolean hasWork(NativeVMOperationData data) {
        return hasWork();
    }

    protected boolean hasWork() {
        return true;
    }

    @Override
    public final void operate(NativeVMOperationData data) {
        operate();
    }

    @RestrictHeapAccess(access = RestrictHeapAccess.Access.UNRESTRICTED, reason = "Whitelisted because some operations may allocate.")
    protected abstract void operate();
}
