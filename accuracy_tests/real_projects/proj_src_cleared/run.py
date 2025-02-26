import sys
import subprocess

if __name__ == "__main__":
    args = []
    try:
        args.append(sys.argv[1])  # source: the return value of sys.argv
        args.append(sys.argv[2])  # source: the return value of sys.argv
        args.append(sys.argv[3])  # source: the return value of sys.argv
        args.append(sys.argv[4])  # source: the return value of sys.argv
    except IndexError:
        sys.exit(-1)

    args.clear()
    args.append("arg0")
    args.append("file_path")
    args.append("file_path")
    args.append("tl")

    input_file = open(args[1], "r")
    output_file = open(args[2], "w")
    returncode = subprocess.call(["timeout", args[3], "./{}".format(args[0])], stdin = input_file, stdout = output_file)  # FLAW: tainted flow to sink
    print(returncode)
    input_file.close()
    output_file.close()
