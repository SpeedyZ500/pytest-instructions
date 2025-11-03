# pytest-instructions

This project assumes that you have VS Code installed already. 
Make sure you have the Pytest extension installed.
## Table of Contents
- [0. Creating and using a Virtual Environment](#0-creating-and-using-a-virtual-environment)
  - [0.1 Setup](#01-setup)
  - [0.2 Activating a Virtual Environment](#02-activating-a-virtual-environment)
- [1 Installing Pytest](#1-installing-pytest)
- [2 Creating a Test File](#2-creating-a-test-file)

## 0 Creating and using a Virtual Environment

**If you already have a virtual Environment set up you can skip to section 1**

### 0.1 Setup
To set up a virtual environment on PC use 

```bash
python -m venv .venv
```
and if on a Mac or a computer configured to use Linux then you should type
```bash
python3 -m venv .venv
```
This creates a hidden directory called `.venv` in your project folder containing a standalone Python environment.

### 0.2 Activating a virtual environment
You now have to tell VSCode that you want to use the virtual environment. This is called _activating_ the environment. How you activate `venv` depends on your machine.

For a Windows machine running PowerShell,
```powershell
venv\Scripts\Activate.ps1
```

and on a Mac or Linux-based machine
```bash
source .venv/bin/activate
```

## 1 Installing Pytest

In your virtual environment, type the command on Windows:

```bash
pip install pytest
```

For MacOS and Linux:

```bash
pip3 install pytest
```

## 2 Creating a test file

To create a test file, you must follow a specific naming scheme. it must begin with ```test_``` or end with ```_test```.
The file extension for your test file should be ```.py```, because it is a python file. 
**The Test file must be separate from your code file.** For these instruction we have provided example test files, and a test file you can edit, to write your own tests, as well as starter code.

## 3 Writing a Basic Positive Test



## 4 Writing a Basic Negative Test



## 5 Testing Classes

When testing a class there are additional things you should be testing other than simply the returned data. 
These are the **Side effects**, the contents of the class that is changed by the function being tested.

## 6 Using Fixtures



## 7 Test Class

There are ways to group tests together, this is particularly useful when testing related methods. 
However class attributes are also shared between tests of the same class, so you must once again use fixtures to prevent side effects and inconsistent testing.
Instance attributes are not shared between tests, so they can be overwritten without fear.

This is fine
```py
class TestClassExample:
    value = 1
    def test_class_example_1(self):
        self.value = 2
        assert self.value == 2
    def test_class_example_2(self):
        assert self.value == 1
```

This is not

```py
class TestScoreKeeper:
    score_obj = ScoreKeeper()
    def test_show_class_effects_1(self):
        #Given
        points_to_add = 7
        expected = 7
        #then
        result = self.score_obj.add_points(points_to_add)
        assert result == expected
        assert self.score_obj.total_score == expected

    def test_show_class_effects_2(self):
        #Given
        points_to_add = 8
        expected = 8
        #then
        result = self.score_obj.add_points(points_to_add)
        assert result == expected
        assert self.score_obj.total_score == expected
```

To make a Test Class or group you only need do one thing

### 7.1 Writing a Test Class

Instantiate a test class using the naming scheme Test*, where you put the name of the test class group after.

```py
class TestClassExample:
```

### 7.2 Writing Tests within a class

Like all methods within any class, you will need to include the self reference, the rest is exactly as before.

```py
class TestAddAB:
    def test_add_a_and_b_both_numeric(self):
        #Given
        a = 5
        b = 12.0
        expected = 17.0
        #Then
        result = add_a_and_b(a, b)
        assert result == expected

    def test_add_a_and_b_not_numeric_reject(self):
        #Given
        a = [1,3,5]
        b = "whatever"
        #Then
        with pytest.raises(TypeError):
            add_a_and_b(a, b)
```

using TestClasses can be a good way to group the positive and negative test cases for functions together.



## 8 Parameterizing Tests

