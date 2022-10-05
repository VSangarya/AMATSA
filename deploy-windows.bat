@echo off

rem change working dir to script directory
cd /D "%~dp0"
python -m venv .venv
source .venv/bin/activate
source .venv/Scripts/activate
pip install -r requirements.txt
pip install -e .
schtasks /f /create /tn amatsa-client /tr "%~dp0\.venv\bin\python.exe %~dp0\src\driver.py" /sc MINUTE /mo %1

exit /B 0

:end
exit /B 1
