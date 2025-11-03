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

## 6 Test Class

There are ways to group tests together, this is particularly useful when testing related methods.



## 7 Using Fixtures



## 8 Parameterizing Tests



