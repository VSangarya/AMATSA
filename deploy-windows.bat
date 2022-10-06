@echo off

rem change working dir to script directory
cd /D "%~dp0"
FOR /f %%p in ('where python') do SET PYTHONPATH=%%p
python -m venv .venv
pip install -r requirements.txt
pip install -e .
schtasks /f /create /tn amatsa-client /tr "%PYTHONPATH% %~dp0src\driver.py" /sc>

exit /B 0

:end
exit /B 1
