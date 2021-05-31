@echo off
pushd %~dp0

set "exe=%cd%\exe\"
set "src=%cd%\src\"

echo Updating UIs
pyuic5 "%exe%gui.ui" -o "%src%gui.py"

echo Running script
python "%src%chatcat.py"

pause