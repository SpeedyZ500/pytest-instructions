# Pytest Demo Instructions

## Introduction

This instruction will guide you through step-by-step instructions of writing `pytest` tests for a demo program and using them to debug errors. At the end of the instruction, there is a practice for you to test creating and using `pytest` tests.

## Table of Contents

- [Pytest Demo Instructions](#pytest-demo-instructions)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [-1 Download the Starter Code](#-1-download-the-starter-code)
  - [0 Create a Virtual Environment](#0-create-a-virtual-environment)
    - [0.1 Setup the Virtual Environment](#01-setup-the-virtual-environment)
    - [0.2 Activate your Virtual Environment](#02-activate-your-virtual-environment)
  - [1 Install Pytest](#1-install-pytest)
  - [2 Create a Test File](#2-create-a-test-file)
  - [3 Write a Positive Test](#3-write-a-positive-test)
  - [4 Write a Negative Test](#4-write-a-negative-test)
  - [5 Test Classes](#5-test-classes)
  - [6 Add Fixtures](#6-add-fixtures)
  - [7 Test Classes](#7-test-classes)
    - [7.1 Write a Test Class](#71-write-a-test-class)
    - [7.2 Write Tests Within a Class](#72-write-tests-within-a-class)
  - [8 Parameterize Tests](#8-parameterize-tests)
  - [9 ✍️ Practice](#9-️-practice)

## Prerequisites

For this demo, you should have [Visual Studio Code](https://code.visualstudio.com/) installed already. You should also have the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed; this extension comes with support for integrading the IDE with the `pytest` framework.

## -1 Download the Starter Code

This repository contains the starter code for this instruction. You will be debugging and creating tests with these files.

1. Run the following command to clone this repository to your computer.

    ```bash
    git clone https://github.com/SpeedyZ500/pytest-instructions.git
    ```

2. Open the repository in VS Code.

## 0 Create a Virtual Environment

We will be using a virtual Python environment called `venv` to ensure consistent Python behavior across operating systems.

>[!NOTE]
>If you already have a virtual environment set up, skip to section 1.

### 0.1 Setup the Virtual Environment

1. Open a command terminal in your project folder.

    >[!NOTE]
    > Any standard command terminal such as Powershell or Bash will work for this demo.

2. Run the following command to set up `venv` on your machine.

    **Windows:**

    ```powershell
    python -m venv .venv
    ```

    **MacOS or Linux:**

    ```bash
    python3 -m venv .venv
    ```

This creates a hidden directory called `.venv` in your working directory containing a standalone Python environment.

### 0.2 Activate your Virtual Environment

You now have to tell VS Code that you want to use the virtual environment. This is called _activating_ the environment.

1. Run the following command to activate `venv` on your machine.

    **Windows:**

    ```powershell
    ./.venv/Scripts/Activate.ps1
    ```

    **MacOS or Linux:**

    ```bash
    source .venv/bin/activate
    ```

## 1 Install Pytest

1. Run the following command to install `pytest` in your virtual enviroment.

    **Windows:**

    ```powershell
    pip install pytest
    ```

    **MacOS or Linux:**

    ```bash
    pip3 install pytest
    ```

## 2 Create a Test File

The

1. Navigate to `demo/`

`pytest` testing files must follow a specific naming scheme. They must be begin with `test_` or end with `_test`.
The file extension for your test file should be `.py`, because it is a python file. For these instruction we have provided example test files, and a test file you can edit, to write your own tests, as well as starter code.

## 3 Write a Positive Test

## 4 Write a Negative Test

## 5 Test Classes

When testing a class there are additional things you should be testing other than simply the returned data.
These are the **Side effects**; the contents of the class that is changed by the function being tested.
Therefore it is important to test that the attributes change as you expect them to.

## 6 Add Fixtures

## 7 Test Classes

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

### 7.1 Write a Test Class

Instantiate a test class using the naming scheme Test*, where you put the name of the test class group after.

```py
class TestClassExample:
```

### 7.2 Write Tests Within a Class

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

## 8 Parameterize Tests

You may need to test several functions that are similar, perhaps they are two children of the same abstract class, which should preform the same operation, but in different ways. Or perhaps you have many functions that have similar data requirements, just slightly different parameters are required. Parameterizing tests can be used in both of these cases. This is also useful when you want to make sure that it works for a variety of inputs, allowing for the testing of edge cases.
It is also possible to parameterize Fixtures, and it will behave in much the same way.

For practice you could write tests for the PriorityQueue test class, using parameterization, and debugging to figure out why the HeapPQ fails a test that LinearPQ passes.

## 9 ✍️ Practice
