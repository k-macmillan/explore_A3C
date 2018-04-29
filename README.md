# Exploring A3C

This is an exploration into A3C with no spatial data.

## Goals
- [ ] Simple environment
- [ ] Build A3C based on Google's [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/pdf/1602.01783.pdf) paper
- [ ] Build more complicated enviroment to test the limits
- [ ] Write paper about methods tested

subgoal: 
Test everything and make it look nice when testing.

## Dependencies
- [Python3](https://www.python.org/download/releases/3.0/)
- [TensorFlow](https://www.tensorflow.org/)
- [colorama](https://github.com/tartley/colorama)

Note:
If you use the Windows command prompt the test output will still be correct but will have extra characters. It is suggested that you use Git Bash or an equivalent. If someone knows how to tell which terminal the user is in then I can fix this, otherwise it stays as is.

### Simple Unit Tests
Each unit test file can be ran individually or all can be ran together with `run_tests.py`. If any of the test files are called with a `-true` argument it will continue to run on failure, but will note the failure.

![Basic example of Unit Tests](images/test_examples.png "Unit Test example")

