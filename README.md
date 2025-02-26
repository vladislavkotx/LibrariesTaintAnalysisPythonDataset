# Taint Analysis Evaluation Data

This repository provides a python dataset containing cases where tainted data flows through library or built-in call invocations

## Repository structure

### `\accuracy_tests` folder

Contains labelled sample Python sources for specific dataflow scenarios.
This is handcrafted mini-projects aimed at verifying precision of the analysis.

The source files contain comments specifying expected issues to be discovered: 
```python
os.system(array1)     #FLAW: tainted flow to sink
```

Additionaly each project contains `expected.txt` file listing all expected problem lines:
```
numpy_array_test.py:8 Command injection
numpy_array_test.py:25 Command injection
```

`accuracy_tests\real_project` folder contains several copied open-source projects

### `\performance_tests` folder

Contains several large projects to evaluate analysis time mainly.

### `\reports` folder

Contains baseline analysis results produced by target analyzer.

#### Reports format
```
TestPack               Name of test pack
TotalCases             Amount of projects in the test
Time,sec               Time for pack analysis
FP,%                   Rate of defects we do not expect to report, but we report them across all pack cases
FN,%                   Rate of defects we expect to report, but we do not report them across all pack cases
Passed,%               Rate of defects we expect to report and we report them across all pack cases
Defects N              Amount of reported defect across all pack cases
PackCases: [           List of pack cases
  {
    Case                     Name of test case
    Time,sec                 Time for case analysis
    FP,%                     Rate of defects we do not expect to report, but we report them in test case
    FN,%                     Rate of defects we expect to report, but we do not report them in test case
    Passed,%                 Rate of defects we expect to report and we report them in test case
    Defects N                Amount of reported defects in test case
    Defects: [               List of reported defects in test case  for Typescript (node.js 16)
      path/to/file.py:(FileLineNumber) (Defect description)
    ]
    Files                    Amount of analyzed files in test case
    LOC                      Amount of lines of code in test case
  }, 
  ...
]    
```
