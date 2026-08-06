@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
echo 如果运行程序后报错，请运行build2.bat
echo 当前版本:Beta-3.3.0
echo 请不要以管理员身份运行buil312d.bat和build312-2.bat！
python3.12 -m PyInstaller --onefile --windowed --uac-admin --name=Keystrokes --icon=icon.ico main.py
pause