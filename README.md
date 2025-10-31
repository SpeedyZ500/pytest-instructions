# pytest-instructions

This project assumes that you have VS Code installed already. 
Make sure you have the Pytest extension installed.

## 1 Creating and using a Virtual Environment

**If you already have a virtual Environment set up you can skip to section 2**

### 1.1 Setup
To set up a virtual environment on PC use 

```bash
python -m venv .venv
```
and if on a Mac or a computer configured to use Linux then you should type
```bash
python3 -m venv .venv
```
This creates a hidden directory called `.venv` in your project folder containing a standalone Python environment.

### 1.2 Activating a virtual environment
You now have to tell VSCode that you want to use the virtual environment. This is called _activating_ the environment. How you activate `venv` depends on your machine.

For a Windows machine running PowerShell,
```powershell
venv\Scripts\Activate.ps1
```

and on a Mac or Linux-based machine
```bash
source .venv/bin/activate
```

## 2 Installing Pytest

In your virtual environment, type the command on Windows:

```bash
pip install pytest
```

For MacOS and Linux:

```bash
pip3 install pytest
```


