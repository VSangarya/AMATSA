@echo off

rem change working dir to script directory
cd /D "%~dp0"
FOR /f %%p in ('where python') do SET PYTHONPATH=%%p
cmd /C %~dp0.venv/Scripts/activate
python -m venv .venv
pip install -r requirements.txt
pip install -e .
cmd /C schtasks /f /create /tn amatsa-client /tr "%~dp0.venv\Scripts\python.exe %~dp0src\driver.py" /sc MINUTE /mo %1
rem cmd /C schtasks /f /create /tn amatsa-client /tr "%PYTHONPATH% %~dp0src\driver.py" /sc MINUTE /mo %1
powershell -Command "& {$set = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries; Set-ScheduledTask -TaskName "amatsa-client" -Settings $set;}"

exit /B 0

:end
exit /B 1
