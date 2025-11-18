# Instructions for debugging a demo using `pytest` Python library basics in VS Code

## Introduction

This instruction will guide you through step-by-step instructions of writing `pytest` tests for a demo program and using them to debug errors. At the end of the instruction, there is a practice for you to test creating and using `pytest` tests.

## Table of Contents

- [Instructions for using the `pytest` Python library to create, execute, and debug code tests for a `pytest` demo in VS Code](#instructions-for-using-the-pytest-python-library-to-create-execute-and-debug-code-tests-for-a-pytest-demo-in-vs-code)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Why learn `pytest`?](#why-learn-pytest)
  - [0 Download the Starter Code](#0-download-the-starter-code)
  - [1 Create a Virtual Environment](#1-create-a-virtual-environment)
    - [1.1 Setup the Virtual Environment](#11-setup-the-virtual-environment)
    - [1.2 Activate your Virtual Environment](#12-activate-your-virtual-environment)
  - [2 Install Pytest](#2-install-pytest)
  - [3 Create a Test File](#3-create-a-test-file)
  - [4 Implement `assert` and `pytest.raises`](#4-implement-assert-and-pytestraises)
  - [5 Run a Test File with `pytest`](#5-run-a-test-file-with-pytest)
    - [5.1 Configure Python Tests](#51-configure-python-tests)
    - [5.2 Run `pytest`](#52-run-pytest)
  - [6 Implement a Positive Test](#6-implement-a-positive-test)
    - [6.1 Write a Positive Test](#61-write-a-positive-test)
    - [6.2 Run a Positive Test](#62-run-a-positive-test)
    - [6.3 Implement Fixes](#63-implement-fixes)
  - [7 Implement a Negative Test](#7-implement-a-negative-test)
    - [7.1 Write a Negative Test](#71-write-a-negative-test)
    - [7.2 Run a Negative Test](#72-run-a-negative-test)
  - [8 Implement Positive and Negative Tests](#8-implement-positive-and-negative-tests)
    - [8.1 Write Positive and Negative Tests](#81-write-positive-and-negative-tests)
    - [8.2 Run Positive and Negative Tests](#82-run-positive-and-negative-tests)
    - [8.3 Implement Fixes](#83-implement-fixes)
  - [9 Review](#9-review)
  - [10 ✍️ Practice](#10-️-practice)

## Prerequisites

- You should have [Visual Studio Code](https://code.visualstudio.com/) installed already.
- You should have [Python](https://www.python.org/downloads/) installed on your system.
- You should have the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed; this extension comes with support for integrading the IDE with the `pytest` framework.

## Why learn `pytest`?

`pytest` is a Python library that helps programmers create, execute, and debug tests for their code. Tests are programs that execute parts of your main program to assert that they are working correctly. This technique gives programmers confidence that their code not only does not throw unexpected errors, but that it does not return unexpected results.

## 0 Download the Starter Code

This repository contains the starter code for this instruction. You will be debugging and creating tests with these files.

1. Run the following command to clone this repository to your computer.

    ```bash
    git clone https://github.com/SpeedyZ500/pytest-instructions.git
    ```

> [!TIP]
> You can copy-and-paste the commands and code snippets in this demo to ensure that your commands
> and code snippets match these instructions exactly.

2. Run the following command to open the repository in VS Code.

    ```bash
    code pytest-instructions
    ```

## 1 Create a Virtual Environment

A good practice for creating a testing environment is to account for variability of python operation across different operating systems. In this demo, you will be using a virtual Python environment called `venv` to ensure consistent Python behavior across operating systems.

> [!NOTE]
> If you already have a virtual environment set up, skip to section 1.

### 1.1 Setup the Virtual Environment

1. Open a command terminal in your project folder in VS Code.

> [!IMPORTANT]
>
> You can open a command terminal in VS Code several ways.
> 1. In the menu bar at the top of VS Code, click `Terminal` > `New Terminal`.
> 2. Or, use the keyboard shortcut <kbd>Ctrl</kbd> + <kbd>`</kbd>.
>
> Any standard command terminal such as PowerShell or Bash will work for this demo.

2. Run the following command in VS Code to set up `venv` on your machine.

    **Windows:**

    ```powershell
    python -m venv .venv
    ```

    **MacOS or Linux:**

    ```bash
    python3 -m venv .venv
    ```

This creates a hidden directory called `.venv` in your working directory containing a standalone Python environment.

### 1.2 Activate your Virtual Environment

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

    You will know that the virtual environment has been successfully activated when you see `(.venv)` on the next line of the terminal.

> [!NOTE]
> If you are are following these instructions on Windows, running the above command may result in an error
> saying that "execution of scripts is disabled on this system." This is because the command that activates
> the virtual environment runs a series of PowerShell commands that sets up the virtual environment.
>
> If this error occurs, follow [these instructions](https://easyentra.com/running-scripts-is-disabled-on-this-system/) to allow the execution of scripts on your Windows system, and then re-run the above command.

## 2 Install Pytest

1. Run the following command to install `pytest` in your virtual enviroment.

    **Windows:**

    ```powershell
    pip install pytest
    ```

    **MacOS or Linux:**

    ```bash
    pip3 install pytest
    ```

    Now that you have `pytest` installed, you are ready to start writing and running tests.

## 3 Create a Test File

The demo Python class for this instruction is a class named `SongLibrary` that is located in [`demo/song_library/song_library.py`](/demo/song_library/song_library.py). It is designed provide functionality to:

- add new songs
- remove songs
- get songs based on genre

To verify that `SongLibrary` is working as expected, this instruction will walk you through debugging `SongLibrary` using `pytest`.

> [!NOTE]
> `pytest` testing files must follow a specific naming scheme. They must be begin with `test_` or end with `_test`.
>
> The file extension for your test file should be `.py` because it is a python file.

1. Create a new file named `test_song_library.py` in the [`song_library`](/demo/song_library) folder.
2. Paste the following starter code into `test_song_library.py`:

    ```py
    import pytest
    from .song_library import Song, SongLibrary

    song_library = SongLibrary()

    # ======== add_song tests ========

    # 🟢 Positive Test
    def test_add_valid_song():
        song_library.clear()
        song_library.add_song(Song("We Built This City", "Rock"))

    # 🔴 Negative Test
    def test_add_invalid_song():
        song_library.clear()

    # ======== remove_song tests ========

    # 🟢 Positive Test
    def test_remove_present_song():
        # TODO: Impelement
        raise NotImplementedError

    # 🔴 Negative Test
    def test_remove_absent_song():
        # TODO: Impelement
        raise NotImplementedError

    # ======== get_songs_in_genre tests ========

    # 🟢 Positive Test
    def test_get_present_song_in_genre():
        # TODO: Impelement
        raise NotImplementedError

    # 🔴 Negative Test
    def test_get_absent_song_in_genre():
        # TODO: Impelement
        raise NotImplementedError
    ```

    This code tests positive (passing) and negative (failing) functionality of three `SongLibrary` methods: `add_song`, `remove_song`, and `get_songs_in_genre`. The starter code above provides nearly complete positive and negative tests for `add_song`.

## 4 Implement `assert` and `pytest.raises`

To assure test results are as expected, you will use two types of statements:

- `assert` statements verify that a condition is true, and if not, an error is raised and the `pytest` test fails.
- `pytest.raises` is a function in the `pytest` library that expects an error to be thrown from your testing methods. If the the method doesn't err or gives an unexpected error, the `pytest` test will fail.

You will add an `assert` statement and a `pytest.raises` statement to the `add_song` tests to complete their implementation.

1. Add the following line of code to the end of `test_add_valid_song`:

    ```py
    assert 1 == len(song_library.songs)
    ```

    This line will verify that the song `"We Built This City"` was actually added to the `SongLibrary` by checking its length. If the length of `song_library.songs` is `1`, the test will pass.

2. Add the following lines of code to the end of `test_add_invalid_song`:

    ```py
    with pytest.raises(TypeError):
        song_library.add_song(67) # type: ignore
    ```

    This line will attend to add an input of the wrong type to the `SongLibrary` and expect a `TypeError` to be thrown. If a `TypeError` is thrown, the test will pass.

> [!IMPORTANT]
> Copy-and-pasting may accidentally remove the indent before the line `song_library.add_song(67) # type: ignore`.
> If this occured, make sure to add the indent back where you pasted the line in `test_son_library.py`.

> [!TIP]
> Adding `# type: ignore` to a line of Python code will signal to the Python IntelliSense to ignore the intentional type error. This won't change the program output, but it keeps an error from appearing in the editor.

## 5 Run a Test File with `pytest`

Now that you have created a test file, you can configure VS Code to discover and execute your tests.

### 5.1 Configure Python Tests

1. Open the Testing tab in VS Code.

> [!IMPORTANT]  
> The button to access the Testing tab is located on the Activity Bar on left side of the screen.
> The icon for the Testing tab is a beaker (![Testing tab beaker icon](images/testing_tab_icon.png)).
2. Press the "Configure Python Tests" button. A dropdown menu will appear at the top of the screen.
3. Select `pytest` as the enabled testing framework.
4. Select the demo directory `demo` as the test directory.

> [!IMPORTANT]
> If you want to change a test directory for `pytest`, you can navigate to `.vscode/settings.json` and switch the value in `"python.testing.pytestArgs"` from `demo` to your chosen folder. To run `pytest` tests on all folders in the repository, set the test directory to `.`, the root directory.

VS Code is now configured to automatically discover any test files and tests in your demo directory.

### 5.2 Run `pytest`

1. Press the "Run Tests" button (![Testing tab Run Tests button icon](images/run_tests_button.png)) in the Testing tab. This will run the `SongLibrary` tests you added in the previous section.

    Notice that all of the tests except for `test_add_valid_song` and `test_add_invalid_song` will fail due to a `NotImplementedError` being thrown.

> [!NOTE]
> A `NotImplementedError` in Python notes functionality that has not yet been fully implemented.
>
> In this instruction, you will be replacing the occurences of `NotImplementedError` with code to debug `SongLibrary`.

Now that you can run `pytest`, you will implement a positive and negative test in `test_song_library.py`.

## 6 Implement a Positive Test

Positive tests assert that programs function as expected given valid input.

### 6.1 Write a Positive Test

The first positive test that you will implement is for the `remove_song` method in `SongLibrary`. It will provide valid inputs and assert that the method runs as expected.

1. Replace `test_remove_present_song` with the following code:

    ```py
    def test_remove_present_song():
        song_library.clear()
        song_library.add_song(Song("We Built This City", "Rock"))
        song_library.remove_song("We Built This City")

        assert 0 == len(song_library.songs)
    ```

    The above test will

    - run `clear` on the testing `SongLibrary` to remove songs left over from other tests.
    - add a new `Rock` song named `"We Built This City"` to the testing `SongLibrary`.
    - remove a song named `"We Built This City"`.
    - assert that the testing `SongLibrary` is empty.

### 6.2 Run a Positive Test

1. Press the "Run Tests" button in the Testing tab to re-run all tests. Even though `test_remove_present_song` is now implemented, it will still fail. You will check the test output to see why the test failed.
2. Open the `test_song_library.py` file.
3. Click the red arrow to the right of `test_remove_present_song`. The arrow will expand into the test output.
4. Look at the test output. The output will explain why `test_remove_present_song` failed.

    The error will look something like the following:

    ```py
            song_library.clear()
            song_library.add_song(Song("We Built This City", "Rock"))
    >       song_library.remove_song("We Built This City")

    song_library\test_song_library.py:23: 
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = Library(["We Built This City"]), song_name = 'We Built This City'

        def remove_song(self, song_name:str) -> None:
        
            for i in range(len(self.songs)):
                if self.songs[i].name == song_name:
    >               self.songs.remove(i) # type: ignore
                    ^^^^^^^^^^^^^^^^^^^^
    E               ValueError: list.remove(x): x not in list

    song_library\song_library.py:38: ValueError
    ```

    From these results, you can see that the test failure was caused by a `ValueError` in of `song_library.py`.

Now that you can identify an error in the code, you can try to implement a fix for the error.

### 6.3 Implement Fixes

1. Open `song_library.py`.
2. Locate the `remove_song` method in the `SongLibrary` class.

    The line which raised a `ValueError` is intended to remove the `Song` from `SongLibrary` at index `i`. This line calls `songs.remove`. The `remove` method on `songs` removes a `Song` that matches an input value to `remove`. However, this line is intended to remove a song based on its index, not its value.

    The correct method, then, is `songs.pop`, which removes `Song` elements based on index.
3. Replace the `self.songs.remove(i)` line of `song_library.py` with

    ```py
    self.songs.pop(i)
    ```

4. Press the "Run Tests" button in the Testing tab to re-run all tests. `test_remove_present_song` is now passing.

You have created and implemented a positive test. The next section will instruct you in writing a test for testing program functionality with invalid inputs.

## 7 Implement a Negative Test

Negative tests assert that programs function as expected given invalid or incorrect input.

### 7.1 Write a Negative Test

The first negative test that you will implement is for the `remove_song` method in `SongLibrary`. It will provide incorrect input and assert that the method runs as expected.

1. Replace `test_remove_absent_song` with the following code:

    ```py
    def test_remove_absent_song():
        song_library.clear()
        song_library.remove_song("The Unsung Song")

        assert 0 == len(song_library.songs)
    ```

    The above test will

    - run `clear` on the testing `SongLibrary` to remove songs left over from other tests.
    - assert no errors when removing a non-existent song `"The Unsung Song"`.

### 7.2 Run a Negative Test

1. Press the "Run Tests" button in the Testing tab to re-run all tests. The Testing tab will show that `test_remove_absent_song` succeeded. Because it succeeded, you will not have to implement any additional fixes in `remove_song`.

You will now implement positive and negative tests for the `get_songs_in_genre` method and implement fixes.

## 8 Implement Positive and Negative Tests

### 8.1 Write Positive and Negative Tests

1. Replace `test_get_present_song_in_genre` with the following code:

    ```py
    def test_get_present_song_in_genre():
        song_library.clear()
        song_library.add_song(Song("We Built This City", "Rock"))
        song_library.add_song(Song("Hello World", "Pop"))
        song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

        assert 1 == len(song_library.get_songs_in_genre("Rock"))
    ```

    The above test will

    - run `clear` on the testing `SongLibrary` to remove songs left over from other tests.
    - add three new songs to the testing `SongLibrary`:
      - a `Rock` song named `"We Built This City"`
      - a `Pop` song named `"Hello World"`
      - a `Country` song named `"Take Me Home, Country Roads"`
    - assert that the testing `SongLibrary` has one `Rock` song.

2. Replace `test_get_absent_song_in_genre` with the following code:

    ```py
    def test_get_absent_song_in_genre():
        song_library.clear()
        song_library.add_song(Song("We Built This City", "Rock"))
        song_library.add_song(Song("Hello World", "Pop"))
        song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

        assert 0 == len(song_library.get_songs_in_genre("Classical"))
    ```

    The above test will

    - run `clear` on the testing `SongLibrary` to remove songs left over from other tests.
    - add three new songs to the testing `SongLibrary`:
      - a `Rock` song named `"We Built This City"`
      - a `Pop` song named `"Hello World"`
      - a `Country` song named `"Take Me Home, Country Roads"`
    - assert that the testing `SongLibrary` has no `Classical` songs.

### 8.2 Run Positive and Negative Tests

1. Press the "Run Tests" button in the Testing tab to re-run all tests. The `test_get_absent_song_in_genre` test will pass, but `test_get_present_song_in_genre` will fail.
2. Open the `test_song_library.py` file.
3. Click the red arrow to the right of `test_get_present_song_in_genre`. The arrow will expand into the test output.
4. Look at the test output. The output will explain why `test_get_present_song_in_genre` failed.

    The error will look something like the following:

    ```py
    song_library.clear()
            song_library.add_song(Song("We Built This City", "Rock"))
            song_library.add_song(Song("Hello World", "Pop"))
            song_library.add_song(Song("Take Me Home, Country Roads", "Country"))

    >       assert 1 == len(song_library.get_songs_in_genre("Rock"))
    E       assert 1 == 0
    E        +  where 0 = len([])
    E        +    where [] = get_songs_in_genre('Rock')
    E        +      where get_songs_in_genre = Library(["We Built This City", "Hello World", "Take Me Home, Country Roads"]).get_songs_in_genre

    demo\song_library\test_song_library_solution.py:45: AssertionError
    ```

    From these results, you can see that the test failure was caused by an `AssertionError` in `song_library.py`. `song_library.get_songs_in_genre("Rock")` did not return any songs.

Now that you can identify an error in the code, you can try to implement a fix for the error.

### 8.3 Implement Fixes

1. Open `song_library.py`.
2. Locate the `get_songs_in_genre` method in the `SongLibrary` class.

    The `AssertionError` reveals that the `get_songs_in_genre` method is not working correctly, but it doesn't give specific detail on the source of the bug. If you look at the contents of the method, you will see the following loop in the code, designed to compare the `genre` of songs in the `SongLibrary` with the provided `genre`.

    ```py
    for i in range(len(self.songs)):
    if self.songs[i].name == genre:
        genre_songs.append(self.songs[i])
    ```

    Notice that the `if` statement compares the `genre` parameter with the `name` of each `Song` instead of the `genre` of each `Song`. The fix for this error would be to reference the `genre` of each `Song`.

3. Replace the expression `self.songs[i].name == genre` in `song_library.py` with

    ```py
    self.songs[i].genre == genre
    ```

4. Press the "Run Tests" button in the Testing tab to re-run all tests. All tests in `test_song_library.py` will now be passing.

## 9 Review

Congratulations on reaching the end of this demo instruction! In this instruction, you

- created and set up a virtual environment with test `pytest` framework
- created a `pytest` test file and ran the tests
- implemented `assert` and `pytest.raises` statements
- implemented positive and negative tests
- used tests to fix errors in code

For additional practice, refer to the assignment below.

## 10 ✍️ Practice

> [!NOTE]
> The practice section of this instruction has not yet been implemented. This is because the authors of this instruction, at the time of writing, are currently working on other computer science coursework. Also, this section is open-ended rather than step-by-step and is therefore not a part of the technical instruction.

<!--

## 8 Write Test Classes

> [!CAUTION]
> This section has not been fully implemented yet.

When testing a class there are additional things you should be testing other than simply the returned data.
These are the **Side effects**; the contents of the class that is changed by the function being tested.
Therefore it is important to test that the attributes change as you expect them to.

## 9 Add Fixtures

> [!CAUTION]
> This section has not been fully implemented yet.

## 10 Test Classes

> [!CAUTION]
> This section has not been fully implemented yet.

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

## 11 Parameterize Tests

> [!CAUTION]
> This section has not been fully implemented yet.

You may need to test several functions that are similar, perhaps they are two children of the same abstract class, which should preform the same operation, but in different ways. Or perhaps you have many functions that have similar data requirements, just slightly different parameters are required. Parameterizing tests can be used in both of these cases. This is also useful when you want to make sure that it works for a variety of inputs, allowing for the testing of edge cases.
It is also possible to parameterize Fixtures, and it will behave in much the same way.

For practice you could write tests for the PriorityQueue test class, using parameterization, and debugging to figure out why the HeapPQ fails a test that LinearPQ passes.
-->
