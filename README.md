# CS:GO Config

## Installation

1. Install Python: https://www.python.org/downloads/
2. Open PowerShell:

`powershell
pip install --user virtualenv
python -m virtualenv env
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\env\Scripts\activate
pip install -r requirements.txt
python .\compile.py
`