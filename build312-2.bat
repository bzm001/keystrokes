@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo ================================================
echo     Keystrokes 按键显示程序打包工具
echo ================================================
echo.

echo 当前版本:Beta-3.3.0
echo 请不要以管理员身份运行build.bat和build2.bat！

:: 检查 Python 3.12 是否存在
python3.12 --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未找到 Python 3.12，请确保已安装并已加入 PATH。
    echo        您也可以修改本脚本中的 python3.12 为合适的命令。
    pause
    exit /b 1
)

:: 显示当前 Python 版本
echo 当前 Python 版本：
python3.12 --version
echo.

:: 安装/更新所需依赖（PyQt5、pynput、pyinstaller）
echo 正在安装/更新 PyInstaller、PyQt5 和 pynput ...
python3.12 -m pip install --upgrade pyinstaller PyQt5 pynput
if errorlevel 1 (
    echo [警告] 依赖安装可能失败，但将继续尝试打包。
)
echo.

:: 开始打包
echo 正在打包程序，请稍候...
python3.12 -m PyInstaller --onefile --windowed --uac-admin --name=Keystrokes --icon=icon.ico --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32 main.py

if errorlevel 1 (
    echo.
    echo [错误] 打包失败！请检查上方错误信息。
    pause
    exit /b 1
)

echo.
echo ================================================
echo     打包成功！
echo     可执行文件位于：dist\Keystrokes.exe
echo ================================================
echo.
echo 提示：运行 Keystrokes.exe 后，配置文件 keystrokes_config.json
echo      会在同目录下自动生成。
pause