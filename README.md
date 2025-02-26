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
