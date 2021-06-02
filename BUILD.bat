@echo off
pushd %~dp0

set "exe=%cd%\exe\"
set "src=%cd%\src\"

pyuic5 "%exe%gui.ui" -o "%src%gui.py"

python build.py

pause