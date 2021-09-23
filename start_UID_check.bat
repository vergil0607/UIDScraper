

set original_dir=%CD%

set venv_root_dir=%original_dir%\venv
cd %venv_root_dir%

call Scripts\activate.bat

set python_path = %original_dir% and "venv\Scripts\python.exe"
set python_file = %original_dir% and "UIDBOT\ValidateUIDs.py"


"%original_dir%\venv\Scripts\python.exe" "%original_dir%\UIDBOT\ValidateUIDs.py"

pause

