@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

set PY_VER=3.12

echo 如果运行程序后报错，请运行build2.bat
echo 当前版本:Release-2.0.0
echo 请不要以管理员身份运行build.bat和build2.bat！
py -%PY_VER% -m PyInstaller --onefile --windowed --uac-admin --name=Keystrokes --icon=icon.ico main.py
pause