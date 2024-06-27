# CS340 Project

## Table of Contents
+ [Overview](#overview)
+ [Requirements](#requirements)
+ [Setting Up Python Virtual Environment](#venv)
+ [Install Requirements](#reqs)
+ [Formatting and Linting](#formatting)
+ [Contributors](#contributors)
+ [README Citation](#citation)

## Overview<a name="overview"></a>
Tbd

## Requirements<a name="requirements"></a>
- Python 3.9+
- VSCode Recommended

# Setting Up Python Virtual Environment<a name="venv"></a>
It is recommended that you use a Python virtual environment for this (and all) Python projects.

## Creating a Python Virtual Environment

### Windows, macOS, and Linux

1. Launch Command Prompt, PowerShell, or your terminal emulator

2. Enter the following command to ensure you have the correct version of Python installed:

    ```bash
    python --version
    ```

    > Depending on your Python configuration, you may need to enter the following command instead:

    ```bash
    python3 --version
    ```

    > Keep track of which command works, and use it for each after this. For brevity, only `python` will be shown in examples.

3. Enter the following command to create a virtual environment named `env`:

    ```bash
    python -m venv env
    ```

    > Optionally, you may specify the Python version for the virtual environment:

    ```bash
    py -3.9 -m venv env
    ```

## Activate the Virtual Environment

### VSCode

1. Open the Command Palette and select `Python: Select Interpreter`
2. Select the interpreter located in the virtual environment `('env':venv)`
3. Reload your terminal

### Windows

- In the PowerShell or Command Prompt, enter the following command to activate the virtual environment:
    
    ```
    cd env\Scripts\
    .\activate
    cd ..\..
    ```

### macOS and Linux

- In the terminal, enter the following command to activate the virtual environment:
    
    ```sh
    source env/bin/activate
    ```

# Install Requirements<a name="reqs"></a>

- Within the virtual environment, enter the following command into the terminal to install all requirements. For all future commands it is assumed that they will be executed from within the virtual environment.
   
    ```bash
    python -m pip install -U -r requirements.txt
    ```

# Formatting and Linting<a name="formatting"></a>
This project uses black for formatting, and flake8 for linting.

- To run black:
   ```bash
   black .
   ```

- To run flake8:
   ```bash
   flake8 .
   ``` 

# Contributors<a name="contributors"></a>
- Wei-Yin Chen `Creativity Officer, Ed Discussion liaison and Submission Proofreader`
- Austin Cooper `Team Leader, Researcher, and Deadline Enforcer`

# README Citation<a name="citation"></a>
README portions ([Requirements](#requirements), [Setting Up Python Virtual Environment](#venv), [Install Requirements](#reqs)) were reused from a previous project. Following is the required citation for CS340.
- URL - none, never hosted anywehere, and exists only on my (Austin Cooper's) hard drive.
- Date retrieved - 6/25/24
- Title - Socket Programming Project 3
- Type - source code
- Author - Austin Cooper
- Code version - N/A