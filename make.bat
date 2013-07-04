@echo off

for %%i in (%cd%) do set project=%%~ni
for /F "tokens=2 delims== " %%i in ('findstr __version__ %cd%\src\%project%\__init__.py') do set version=%%i

python setup.py sdist
python setup.py install
python -m robot.libdoc -F html -v %version:~1,-1% OracleLibrary %cd%\doc\%project%.html