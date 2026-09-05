#!/usr/bin/env python3
#coding:utf-8

# python 3.6 or higher
# python 3.8 or higher is the most stable version
# Python 3.12 is the version used in the development of this project, which may be more stable

# keystrokes

# author: bzm001
# Github: https://github.com/bzm001/keystrokes

"""
========================= Alpha ==========================
Alpha-1.0.0 更新日志:
1. 完善基础功能
Alpha-2.0.0 更新日志:
1. 添加配置文件
2. 优化CPS显示
Alpha-2.1.0 更新日志:
1. 修复更改大小、透明度等选项时出现的严重bug
Alpha-2.2.0 更新日志:
1. 修复配置界面出现纯黑色背景的bug
Alpha-2.3.0 更新日志:
1. 优化系统托盘右键菜单
Alpha-2.3.1 更新日志:
1. 更改了Alpha版本的版本号命名规则，进入Beta阶段
==========================================================

========================== Beta ==========================
Beta-3.0.0 更新日志:
1. 新增程序图标，在build.bat和build2.bat中添加命令
Beta-3.0.1 更新日志:
1. 修改build.bat和build2.bat中的命令，现在不能以管理员身份运行build.bat和build2.bat
Beta-3.0.2 更新日志:
1. 更改配置文件检查逻辑，添加版本号比对与升级询问，添加配置文件中的版本号值
Beta-3.1.0 更新日志:
1. 更改设置界面的标题栏，现在格式为 "按键显示设置 - Version:" + VERSION
Beta-3.1.1 更新日志:
1. 更改设置界面的标题栏变量显示方式，现在更改为了f-string
2. 更改设置界面的标题栏格式，现在格式为 f"Keystrokes - Version:{VERSION}"
Beta-3.1.2 更新日志:
1. 设置窗口背景改为白色
2. 设置窗口字体改为与主窗口一致的字体族（Cascadia Code / Segoe UI / Microsoft YaHei / Arial）
Beta-3.1.3 更新日志:
1. 修复窗口字体问题
Beta-3.1.4 更新日志:
1. 彻底修复设置窗口字体问题（样式表覆盖所有子控件 + 调用 setFont）
Beta-3.1.5 更新日志:
1. 增强配置检查：删除多余键值对，限制scale最小值为0.1，修正x/y为非负，验证颜色有效性
Beta-3.1.6 更新日志:
1. 按键按下反应改为不透明度增加25%，并添加圆角渐变边框
2. 设置界面标签"透明度"改为"不透明度"
Beta-3.1.7 更新日志:
1. 修复边框显示位置问题（修复显示错误，与背景重合）
Beta-3.1.8 更新日志:
1. 为按键按下/松开添加淡入淡出动画效果，时长可在配置文件中自定义（animation_duration）
Beta-3.1.9 更新日志:
1. 修复动画效果未生效及边框渐变色失效的问题
2. 设置界面新增动画时长调节控件
Beta-3.2.0 更新日志:
1. 边框添加独立的淡入淡出效果，松开按键时边框平滑消失
Beta-3.3.0 更新日志:
1. 将按下时的边框加粗（2px → 3px）
2. 现在支持直接运行main.py也可以正常显示图标（在app = QApplication(sys.argv)代码之后添加图标显示逻辑）
3. 将渐变色的gradient_start值修改为#ff0000
4. 添加check_config函数对于animation_duration的检查部分
5. 优化check_config函数对于version的检查部分
6. 添加对xy是否超过屏幕范围的检查
Beta-3.3.1 更新日志:
1. 更改build.bat和build2.bat名称为build312.bat和build312-2.bat
==========================================================

======================== Release =========================
Release-1.0.0 更新日志:
1. 上传代码到GitHub
Release-1.0.1 更新日志:
1. 修复了Release-1.0.0中的版本号错误
2. 修改了版本号检测的1个逻辑
Release-2.0.0 更新日志:
1. 新增版本检测功能，启动时从GitHub获取最新版本并提示更新
2. 设置界面增加“启用版本检查”复选框
3. 支持永久忽略特定版本
4. 修复版本检测对话框显示纯黑背景的问题（将父窗口设为None）
5. 修复配置文件生成位置不正确的问题（改为基于脚本所在目录的绝对路径）
6. 统一图标加载路径，确保与脚本同目录
7. 优化文件详解和目录树
8. 回退了Beta-3.3.1的更改
9. 优化build.bat和build2.bat, 更容易修改python版本, 添加了PY_VER变量
10. 正式支持Python-3.13和Python-3.14
11. 废除了WARNING中的“打包时需要使用python3.12”项
==========================================================
"""

# ======================== WARNING ========================
# - 直接运行程序时至少需要python3.6
# - python3.8或更高版本更加稳定
# - python3.12是开发时使用的版本，可能更加稳定
# =========================================================

"""
二次开发必看!!!

Release-2.0.0 目录树("*"表示无实际用途, "^"表示后期或者运行程序生成的文件):
code
├── build.bat
├── build2.bat
├── icon.ico
├── ^keystrokes_config.json
├── *VERSION
├── *README.md
├── *LICENSE
├── *.gitignore
└── main.py

Release-2.0.0 文件详解("*"表示无实际用途, "^"表示后期或者运行程序生成的文件):
1. build.bat: 打包程序 - 需要python3.12
2. build2.bat: 高级打包程序 - 需要python3.12
3. icon.ico: 程序图标
4. main.py: 主程序 - python3.6+可用, python3.8或更高版本更加稳定, python3.12是开发时使用的版本, 可能更加稳定
5. ^keystrokes_config.json: 配置文件 - 在运行main.py或keystrokes时会自动生成
6. *VERSION: 在本地无实际用途, 在github上为程序提供更新信息, 可以删除本地文件, 不会影响程序运行
7. *README.md: 项目说明文件, 已经了解后可以删除, 不会影响程序运行
8. *LICENSE: 软件许可证文件, 已经了解后可以删除, 不会影响程序运行
9. *.gitignore: git忽略文件, 仅在开发时使用, 可以删除, 不会影响程序运行
"""

import sys
import json
import time
import os
import webbrowser
from collections import deque
from threading import Event

from PyQt5.QtWidgets import (QApplication, QWidget, QSystemTrayIcon, QMenu,
                             QDialog, QSlider, QPushButton, QSpinBox, QDoubleSpinBox,
                             QLabel, QHBoxLayout, QVBoxLayout, QColorDialog,
                             QFormLayout, QDialogButtonBox, QMessageBox, QCheckBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer, QPoint
from PyQt5.QtGui import (QPainter, QColor, QLinearGradient, QPen, QFont,
                         QIcon, QPixmap, QBrush)
from pynput import keyboard, mouse

# ======================== 获取脚本所在目录 ========================
if getattr(sys, 'frozen', False):
    # 打包后的 .exe 环境
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # 开发环境（直接运行 .py）
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================== 默认配置 ========================
CONFIG_FILE = os.path.join(BASE_DIR, "keystrokes_config.json")
VERSION = "Release-2.0.0"

VERSION_LIST = [
    "Alpha-1.0.0",
    "Alpha-2.0.0",
    "Alpha-2.1.0",
    "Alpha-2.2.0",
    "Alpha-2.3.0",
    "Alpha-2.3.1",
    "Beta-3.0.0",
    "Beta-3.0.1",
    "Beta-3.0.2",
    "Beta-3.1.0",
    "Beta-3.1.1",
    "Beta-3.1.2",
    "Beta-3.1.3",
    "Beta-3.1.4",
    "Beta-3.1.5",
    "Beta-3.1.6",
    "Beta-3.1.7",
    "Beta-3.1.8",
    "Beta-3.1.9",
    "Beta-3.2.0",
    "Beta-3.3.0",
    "Beta-3.3.1",
    "Release-1.0.0",
    "Release-1.0.1",
    "Release-2.0.0"
]

DEFAULT_CONFIG = {
    "opacity": 0.5,
    "x": 0,
    "y": 800,
    "gradient_start": "#ff0000",
    "gradient_end": "#ffff00",
    "scale": 0.75,
    "animation_duration": 0.05,
    "version": VERSION,
    "check_for_updates": True,
    "ignored_version": ""
}

# ======================== 配置检查 ========================
def check_config():
    errors = []
    config = {}

    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except Exception as e:
        config = DEFAULT_CONFIG.copy()
        errors.append(f"配置文件不存在或格式错误，已使用默认配置创建 (错误: {e})")

    allowed_keys = set(DEFAULT_CONFIG.keys())
    for key in list(config.keys()):
        if key not in allowed_keys:
            del config[key]
            errors.append(f"移除多余键 '{key}'")

    for key, default in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = default
            errors.append(f"缺失键 '{key}'，已添加默认值")
        else:
            if key in ("opacity", "scale"):
                if not isinstance(config[key], (int, float)) or not (0.0 <= config[key] <= 1.0):
                    config[key] = default
                    errors.append(f"键 '{key}' 值范围错误（应为 0~1），已重置为 {default}")
                if key == "scale" and config[key] == 0.0:
                    config[key] = 0.1
                    errors.append("键 'scale' 值为 0，已修正为最小 0.1")
            elif key in ("x", "y"):
                if not isinstance(config[key], int):
                    config[key] = default
                    errors.append(f"键 '{key}' 类型错误（应为整数），已重置为 {default}")
                else:
                    if config[key] < 0:
                        config[key] = 0
                        errors.append(f"键 '{key}' 为负数，已修正为 0")
            elif key in ("gradient_start", "gradient_end"):
                if not isinstance(config[key], str):
                    config[key] = default
                    errors.append(f"键 '{key}' 类型错误，已重置为 {default}")
                else:
                    color = QColor(config[key])
                    if not color.isValid():
                        config[key] = default
                        errors.append(f"键 '{key}' 颜色值无效，已重置为 {default}")
            elif key == "version":
                if not isinstance(config[key], str):
                    config[key] = default
                    errors.append("版本号格式错误，已重置")
            elif key == "animation_duration":
                if not isinstance(config[key], (int, float)) or config[key] < 0:
                    config[key] = default
                    errors.append(f"键 '{key}' 必须为非负数，已重置为 {default}")
                if config[key] > 0.5:
                    config[key] = default
                    errors.append(f"键 '{key}' 值范围错误（应 ≤ 0.5），已重置为 {default}")
            elif key == "check_for_updates":
                if not isinstance(config[key], bool):
                    config[key] = True
                    errors.append("键 'check_for_updates' 类型错误，已重置为 True")
            elif key == "ignored_version":
                if not isinstance(config[key], str):
                    config[key] = ""
                    errors.append("键 'ignored_version' 类型错误，已重置为空字符串")

    # ========== 屏幕边界检查 ==========
    screen = QApplication.primaryScreen()
    if screen:
        screen_geo = screen.geometry()
        screen_width = screen_geo.width()
        screen_height = screen_geo.height()
        # 修正 x
        if config.get("x", 0) > screen_width:
            config["x"] = DEFAULT_CONFIG["x"]
            errors.append(f"键 'x' 超出屏幕宽度（{screen_width}），已重置为 {DEFAULT_CONFIG['x']}")
        # 修正 y
        if config.get("y", 0) > screen_height:
            config["y"] = DEFAULT_CONFIG["y"]
            errors.append(f"键 'y' 超出屏幕高度（{screen_height}），已重置为 {DEFAULT_CONFIG['y']}")

    # ========== 版本检查 ==========
    current_ver = DEFAULT_CONFIG["version"]
    config_version = config.get("version", "")

    if config_version not in VERSION_LIST:
        errors.append(f"配置文件版本号 '{config_version}' 不在版本列表中，可能已被手动修改")
        reply = QMessageBox.question(
            None,
            "版本错误",
            f"配置文件版本号 '{config_version}' 不在版本列表中，请检查你是否修改了配置文件中的 version 值。\n\n是否继续运行？\n选择「是」将继续（修复版本号），选择「否」退出程序。",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            # 修复版本号
            config["version"] = current_ver
            errors.append(f"版本已修复至 {current_ver}")
        else:
            sys.exit(0)
    elif config_version != current_ver:
        reply = QMessageBox.question(
            None,
            "版本升级",
            f"配置文件版本 ({config_version}) 与程序版本 ({current_ver}) 不一致。\n\n是否自动升级配置文件？\n\n选择「是」升级并继续，选择「否」退出程序。",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            config["version"] = current_ver
            errors.append(f"版本已升级至 {current_ver}")
        else:
            sys.exit(0)

    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    return 0 if not errors else "\n".join(errors)

# ======================== 版本检查线程 ========================
class UpdateCheckThread(QThread):
    finished = pyqtSignal(str)   # 远程版本号
    error = pyqtSignal(str)      # 错误信息

    def run(self):
        try:
            import urllib.request
            url = "https://raw.githubusercontent.com/bzm001/keystrokes/main/VERSION"
            req = urllib.request.Request(url, headers={"User-Agent": "Keystrokes"})
            with urllib.request.urlopen(req, timeout=10) as response:
                data = response.read().decode('utf-8').strip()
                self.finished.emit(data)
        except Exception as e:
            self.error.emit(str(e))

# ======================== 自定义按键控件 ========================
class KeyWidget(QWidget):
    def __init__(self, text, parent=None, width=60, height=60, show_cps=False, scale=1.0, animation_duration=0.05):
        super().__init__(parent)
        self.text = text
        self.show_cps = show_cps
        self.cps_text = "0.0 CPS"
        self.pressed = False
        self.global_opacity = 0.8
        self.gradient_start = QColor("#FFCC00")
        self.gradient_end = QColor("#FF8800")
        self.scale = scale
        self.setFixedSize(width, height)

        # ---- 动画相关 ----
        self.animation_duration = animation_duration
        self.current_opacity = self.global_opacity
        self.target_opacity = self.global_opacity
        self.animation_start_value = self.global_opacity
        self.animation_start_time = 0
        self.animating = False
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.update_animation)
        self.animation_timer.setInterval(16)

        # ---- 边框独立透明度 ----
        self.border_opacity = 0.0
        self.target_border_opacity = 0.0
        self.border_animation_start_value = 0.0

    def set_pressed(self, pressed):
        if self.pressed == pressed:
            return
        self.pressed = pressed
        # 背景目标
        target_bg = min(1.0, self.global_opacity + 0.25) if pressed else self.global_opacity
        # 边框目标：按下时为增亮后的不透明度，松开时为 0
        target_border = min(1.0, self.global_opacity + 0.25) if pressed else 0.0

        # 启动背景动画
        if abs(self.current_opacity - target_bg) < 0.001:
            self.current_opacity = target_bg
            self.target_opacity = target_bg
        else:
            self.animation_start_value = self.current_opacity
            self.target_opacity = target_bg
            self.animation_start_time = time.time()
            self.animating = True
            if not self.animation_timer.isActive():
                self.animation_timer.start()

        # 边框立即开始动画（独立插值）
        self.border_animation_start_value = self.border_opacity
        self.target_border_opacity = target_border
        # 如果边框动画目标与当前值相差很小，直接设定
        if abs(self.border_opacity - target_border) < 0.001:
            self.border_opacity = target_border
        else:
            # 启动边框动画（与背景使用同一个定时器）
            if not self.animating:
                self.animating = True
                self.animation_start_value = self.current_opacity
                self.animation_start_time = time.time()
                if not self.animation_timer.isActive():
                    self.animation_timer.start()

    def update_animation(self):
        if not self.animating:
            self.animation_timer.stop()
            return
        elapsed = time.time() - self.animation_start_time
        duration = self.animation_duration
        if duration <= 0:
            self.current_opacity = self.target_opacity
            self.border_opacity = self.target_border_opacity
            self.animating = False
            self.animation_timer.stop()
            self.update()
            return
        progress = min(1.0, elapsed / duration)
        # 背景插值
        self.current_opacity = self.animation_start_value + (self.target_opacity - self.animation_start_value) * progress
        # 边框插值
        self.border_opacity = self.border_animation_start_value + (self.target_border_opacity - self.border_animation_start_value) * progress
        if progress >= 1.0:
            self.current_opacity = self.target_opacity
            self.border_opacity = self.target_border_opacity
            self.animating = False
            self.animation_timer.stop()
        self.update()

    def set_global_opacity(self, op):
        self.global_opacity = max(0.0, min(1.0, op))
        if not self.animating:
            self.current_opacity = self.global_opacity
            self.target_opacity = self.global_opacity
            # 边框重置为0（因为未按下）
            self.border_opacity = 0.0
            self.target_border_opacity = 0.0
        else:
            # 如果正在动画，停止并重置
            self.current_opacity = self.global_opacity
            self.target_opacity = self.global_opacity
            self.border_opacity = 0.0
            self.target_border_opacity = 0.0
            self.animating = False
            self.animation_timer.stop()
        self.update()

    def set_cps(self, cps):
        self.cps_text = f"{cps:.1f} CPS"
        self.update()

    def set_gradient(self, start_color, end_color):
        self.gradient_start = QColor(start_color)
        self.gradient_end = QColor(end_color)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        alpha = int(self.current_opacity * 255)
        bg_color = QColor(15, 12, 15, alpha)

        painter.setBrush(bg_color)
        painter.setPen(Qt.NoPen)
        rect = self.rect()
        painter.drawRoundedRect(rect, 6, 6)

        # ---- 边框绘制（独立透明度） ----
        if self.border_opacity > 0.001:
            gradient = QLinearGradient(rect.topLeft(), rect.topRight())
            gradient.setColorAt(0, self.gradient_start)
            gradient.setColorAt(1, self.gradient_end)
            brush = QBrush(gradient)
            # 边框宽度从 2 改为 3（加粗）
            pen = QPen(brush, 3)
            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)
            # 边框透明度使用 border_opacity
            border_alpha = int(self.border_opacity * 255)
            painter.setOpacity(border_alpha / 255.0)
            painter.drawRoundedRect(rect, 6, 6)
            painter.setOpacity(1.0)

        # ---- 文字渐变 ----
        gradient = QLinearGradient(rect.topLeft(), rect.topRight())
        gradient.setColorAt(0, self.gradient_start)
        gradient.setColorAt(1, self.gradient_end)
        painter.setPen(QPen(gradient, 1))

        font = painter.font()
        font.setBold(True)
        font.setFamilies(["Cascadia Code", "Segoe UI", "Microsoft YaHei", "Arial"])
        base_size = 12
        cps_base_size = 8
        size = max(8, min(30, int(base_size * self.scale)))
        font.setPointSize(size)
        painter.setFont(font)

        painter.drawText(rect, Qt.AlignCenter, self.text)

        if self.show_cps:
            painter.setPen(QColor(200, 200, 200, alpha))
            cps_font = font
            cps_size = max(6, min(20, int(cps_base_size * self.scale)))
            cps_font.setPointSize(cps_size)
            painter.setFont(cps_font)
            cps_rect = rect
            offset = int(15 * self.scale)
            cps_rect.setTop(rect.height() - offset)
            painter.drawText(cps_rect, Qt.AlignHCenter | Qt.AlignBottom, self.cps_text)

# ======================== 输入监听线程 ========================
class InputListenerThread(QThread):
    key_pressed = pyqtSignal(str)
    key_released = pyqtSignal(str)
    mouse_pressed = pyqtSignal(str)
    mouse_released = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.stop_event = Event()
        self.keyboard_listener = None
        self.mouse_listener = None

    def run(self):
        with keyboard.Listener(on_press=self.on_key_press,
                               on_release=self.on_key_release) as k_listener, \
             mouse.Listener(on_click=self.on_mouse_click) as m_listener:
            self.keyboard_listener = k_listener
            self.mouse_listener = m_listener
            while not self.stop_event.is_set():
                if not k_listener.running or not m_listener.running:
                    break
                self.msleep(50)

    def stop(self):
        self.stop_event.set()
        if self.keyboard_listener:
            self.keyboard_listener.stop()
        if self.mouse_listener:
            self.mouse_listener.stop()

    def on_key_press(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                ch = key.char.lower()
                if ch in ('w', 'a', 's', 'd'):
                    self.key_pressed.emit(ch)
        except:
            pass
        if key == keyboard.Key.space:
            self.key_pressed.emit('space')
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            self.key_pressed.emit('shift')

    def on_key_release(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                ch = key.char.lower()
                if ch in ('w', 'a', 's', 'd'):
                    self.key_released.emit(ch)
        except:
            pass
        if key == keyboard.Key.space:
            self.key_released.emit('space')
        if key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
            self.key_released.emit('shift')

    def on_mouse_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            if pressed:
                self.mouse_pressed.emit('left')
            else:
                self.mouse_released.emit('left')
        elif button == mouse.Button.right:
            if pressed:
                self.mouse_pressed.emit('right')
            else:
                self.mouse_released.emit('right')

# ======================== 设置窗口 ========================
class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main = parent

        font = QFont()
        font.setFamilies(["Cascadia Code", "Segoe UI", "Microsoft YaHei", "Arial"])
        self.setFont(font)

        self.setWindowTitle(f"Keystrokes - Version:{VERSION}")
        self.setModal(True)
        self.setFixedSize(440, 450)  # 高度增加以容纳新控件

        self.setStyleSheet("""
            QDialog, QSpinBox, QSlider, QLabel, QPushButton, QDialogButtonBox, QWidget {
                font-family: "Cascadia Code", "Segoe UI", "Microsoft YaHei", Arial;
                background-color: #ffffff;
            }
            QSpinBox, QSlider, QLabel, QPushButton {
                background-color: #f0f0f0;
                color: #000000;
                border: 1px solid #aaaaaa;
                border-radius: 4px;
                padding: 2px;
            }
            QPushButton {
                background-color: #e0e0e0;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QSlider::groove:horizontal {
                height: 6px;
                background: #cccccc;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #888888;
                width: 14px;
                height: 14px;
                margin: -4px 0;
                border-radius: 7px;
            }
        """)

        layout = QVBoxLayout(self)
        form = QFormLayout()

        self.op_slider = QSlider(Qt.Horizontal)
        self.op_slider.setRange(10, 100)
        self.op_slider.setValue(int(self.main.opacity * 100))
        self.op_slider.valueChanged.connect(self.on_op_slider_changed)

        self.op_spin = QSpinBox()
        self.op_spin.setRange(10, 100)
        self.op_spin.setValue(int(self.main.opacity * 100))
        self.op_spin.setFixedWidth(60)
        self.op_spin.valueChanged.connect(self.on_op_spin_changed)

        op_widget = QWidget()
        op_layout = QHBoxLayout(op_widget)
        op_layout.addWidget(self.op_slider)
        op_layout.addWidget(self.op_spin)
        form.addRow("不透明度 (%):", op_widget)

        self.start_btn = QPushButton("选择颜色")
        self.start_btn.setStyleSheet(f"background-color: {self.main.gradient_start.name()}; color: #000;")
        self.start_btn.clicked.connect(lambda: self.choose_color('start'))
        self.end_btn = QPushButton("选择颜色")
        self.end_btn.setStyleSheet(f"background-color: {self.main.gradient_end.name()}; color: #000;")
        self.end_btn.clicked.connect(lambda: self.choose_color('end'))
        color_widget = QWidget()
        color_layout = QHBoxLayout(color_widget)
        color_layout.addWidget(QLabel("起始:"))
        color_layout.addWidget(self.start_btn)
        color_layout.addWidget(QLabel("结束:"))
        color_layout.addWidget(self.end_btn)
        form.addRow("字体渐变:", color_widget)

        self.x_spin = QSpinBox()
        self.x_spin.setRange(0, 3000)
        self.x_spin.setValue(self.main.x())
        self.x_spin.setFixedWidth(80)
        self.y_spin = QSpinBox()
        self.y_spin.setRange(0, 3000)
        self.y_spin.setValue(self.main.y())
        self.y_spin.setFixedWidth(80)
        pos_widget = QWidget()
        pos_layout = QHBoxLayout(pos_widget)
        pos_layout.addWidget(QLabel("X:"))
        pos_layout.addWidget(self.x_spin)
        pos_layout.addWidget(QLabel("Y:"))
        pos_layout.addWidget(self.y_spin)
        form.addRow("窗口位置:", pos_widget)

        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setRange(50, 200)
        self.scale_slider.setValue(int(self.main.scale * 100))
        self.scale_slider.valueChanged.connect(self.on_scale_slider_changed)

        self.scale_spin = QSpinBox()
        self.scale_spin.setRange(50, 200)
        self.scale_spin.setValue(int(self.main.scale * 100))
        self.scale_spin.setFixedWidth(60)
        self.scale_spin.valueChanged.connect(self.on_scale_spin_changed)

        scale_widget = QWidget()
        scale_layout = QHBoxLayout(scale_widget)
        scale_layout.addWidget(self.scale_slider)
        scale_layout.addWidget(self.scale_spin)
        form.addRow("按键大小 (%):", scale_widget)

        self.anim_slider = QSlider(Qt.Horizontal)
        self.anim_slider.setRange(0, 50)
        self.anim_slider.setValue(int(self.main.animation_duration * 100))
        self.anim_slider.valueChanged.connect(self.on_anim_slider_changed)

        self.anim_spin = QDoubleSpinBox()
        self.anim_spin.setRange(0, 0.5)
        self.anim_spin.setSingleStep(0.01)
        self.anim_spin.setValue(self.main.animation_duration)
        self.anim_spin.setFixedWidth(80)
        self.anim_spin.valueChanged.connect(self.on_anim_spin_changed)

        anim_widget = QWidget()
        anim_layout = QHBoxLayout(anim_widget)
        anim_layout.addWidget(self.anim_slider)
        anim_layout.addWidget(self.anim_spin)
        form.addRow("动画时长 (秒):", anim_widget)

        # ---- 新增：启用版本检查复选框 ----
        self.update_check_cb = QCheckBox("启用版本检查")
        self.update_check_cb.setChecked(self.main.config.get("check_for_updates", True))
        form.addRow(self.update_check_cb)

        layout.addLayout(form)

        btn_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(self.save_settings)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def on_op_slider_changed(self, val):
        self.op_spin.blockSignals(True)
        self.op_spin.setValue(val)
        self.op_spin.blockSignals(False)

    def on_op_spin_changed(self, val):
        self.op_slider.blockSignals(True)
        self.op_slider.setValue(val)
        self.op_slider.blockSignals(False)

    def on_scale_slider_changed(self, val):
        self.scale_spin.blockSignals(True)
        self.scale_spin.setValue(val)
        self.scale_spin.blockSignals(False)

    def on_scale_spin_changed(self, val):
        self.scale_slider.blockSignals(True)
        self.scale_slider.setValue(val)
        self.scale_slider.blockSignals(False)

    def on_anim_slider_changed(self, val):
        value = val / 100.0
        self.anim_spin.blockSignals(True)
        self.anim_spin.setValue(value)
        self.anim_spin.blockSignals(False)

    def on_anim_spin_changed(self, val):
        int_val = int(val * 100)
        self.anim_slider.blockSignals(True)
        self.anim_slider.setValue(int_val)
        self.anim_slider.blockSignals(False)

    def choose_color(self, which):
        initial = self.main.gradient_start if which == 'start' else self.main.gradient_end
        color = QColorDialog.getColor(initial, self, "选择颜色")
        if color.isValid():
            if which == 'start':
                self.main.gradient_start = color
                self.start_btn.setStyleSheet(f"background-color: {color.name()}; color: #000;")
            else:
                self.main.gradient_end = color
                self.end_btn.setStyleSheet(f"background-color: {color.name()}; color: #000;")

    def save_settings(self):
        op = self.op_slider.value() / 100.0
        self.main.set_opacity(op)
        self.main.update_gradient_colors()
        x = self.x_spin.value()
        y = self.y_spin.value()
        self.main.move(x, y)
        scale = self.scale_slider.value() / 100.0
        self.main.set_scale(scale)
        anim_duration = self.anim_spin.value()
        self.main.set_animation_duration(anim_duration)
        # 保存版本检查设置
        self.main.config["check_for_updates"] = self.update_check_cb.isChecked()
        self.main.save_config()
        self.main.raise_()
        self.main.activateWindow()
        self.accept()

# ======================== 主窗口 ========================
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        result = check_config()
        if result != 0:
            print("配置检查报告：\n", result)

        self.config = self.load_config()
        self.opacity = self.config.get("opacity", 0.75)
        self.gradient_start = QColor(self.config.get("gradient_start", "#ff0000"))
        self.gradient_end = QColor(self.config.get("gradient_end", "#ffff00"))
        self.scale = self.config.get("scale", 0.75)
        self.animation_duration = self.config.get("animation_duration", 0.05)

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint |
                            Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

        self.keys = {}
        self.create_keys(self.scale)

        x = self.config.get("x", 0)
        y = self.config.get("y", 846)
        screen = QApplication.primaryScreen()
        screen_geo = screen.geometry()
        screen_width = screen_geo.width()
        screen_height = screen_geo.height()
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        win_width = self.width()
        win_height = self.height()
        if x + win_width > screen_width:
            x = screen_width - win_width
        if y + win_height > screen_height:
            y = screen_height - win_height
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        self.move(x, y)

        self.lmb_clicks = deque()
        self.rmb_clicks = deque()
        self.cps_update_timer = QTimer()
        self.cps_update_timer.timeout.connect(self.update_cps_display)
        self.cps_update_timer.start(200)

        self.listener_thread = InputListenerThread()
        self.listener_thread.key_pressed.connect(self.on_key_pressed)
        self.listener_thread.key_released.connect(self.on_key_released)
        self.listener_thread.mouse_pressed.connect(self.on_mouse_pressed)
        self.listener_thread.mouse_released.connect(self.on_mouse_released)
        self.listener_thread.start()

        self.create_tray_icon()
        self.drag_pos = None

        # ---- 延迟执行版本检查 ----
        self.update_thread = None
        QTimer.singleShot(1500, self.check_for_updates)

    def create_keys(self, scale):
        for key in list(self.keys.values()):
            key.deleteLater()
            key.setParent(None)
        self.keys.clear()
        QApplication.processEvents()

        base_wasd_size = 60
        base_space_w = 200
        base_space_h = 40
        base_shift_w = 200
        base_shift_h = 30
        base_mouse_w = 80
        base_mouse_h = 50
        gap = 5

        wasd_size = int(base_wasd_size * scale)
        space_w = int(base_space_w * scale)
        space_h = int(base_space_h * scale)
        shift_w = int(base_shift_w * scale)
        shift_h = int(base_shift_h * scale)
        mouse_w = int(base_mouse_w * scale)
        mouse_h = int(base_mouse_h * scale)

        margin = 10
        total_w = 3 * wasd_size + 2 * gap + 2 * margin
        total_h = wasd_size + gap + wasd_size + gap + space_h + gap + shift_h + gap + mouse_h + margin
        self.setFixedSize(total_w, total_h)

        center_x = total_w // 2
        w_x = center_x - wasd_size // 2
        w_y = margin
        a_x = center_x - wasd_size - gap - wasd_size // 2
        s_x = center_x - wasd_size // 2
        d_x = center_x + gap + wasd_size // 2
        asd_y = margin + wasd_size + gap

        wasd_map = {
            'w': (w_x, w_y),
            'a': (a_x, asd_y),
            's': (s_x, asd_y),
            'd': (d_x, asd_y)
        }
        for key, (x, y) in wasd_map.items():
            widget = KeyWidget(key.upper(), self, wasd_size, wasd_size, scale=scale,
                               animation_duration=self.animation_duration)
            widget.move(x, y)
            widget.set_global_opacity(self.opacity)
            widget.set_gradient(self.gradient_start, self.gradient_end)
            widget.show()
            self.keys[key] = widget

        space_x = (total_w - space_w) // 2
        space_y = asd_y + wasd_size + gap
        space = KeyWidget("SPACE", self, space_w, space_h, scale=scale,
                          animation_duration=self.animation_duration)
        space.move(space_x, space_y)
        space.set_global_opacity(self.opacity)
        space.set_gradient(self.gradient_start, self.gradient_end)
        space.show()
        self.keys['space'] = space

        shift_x = (total_w - shift_w) // 2
        shift_y = space_y + space_h + gap
        shift = KeyWidget("SHIFT", self, shift_w, shift_h, scale=scale,
                          animation_duration=self.animation_duration)
        shift.move(shift_x, shift_y)
        shift.set_global_opacity(self.opacity)
        shift.set_gradient(self.gradient_start, self.gradient_end)
        shift.show()
        self.keys['shift'] = shift

        mouse_y = shift_y + shift_h + gap
        mouse_total_w = 2 * mouse_w + gap
        mouse_start_x = (total_w - mouse_total_w) // 2
        lmb_x = mouse_start_x
        rmb_x = mouse_start_x + mouse_w + gap

        lmb = KeyWidget("LMB", self, mouse_w, mouse_h, show_cps=True, scale=scale,
                        animation_duration=self.animation_duration)
        lmb.move(lmb_x, mouse_y)
        lmb.set_global_opacity(self.opacity)
        lmb.set_gradient(self.gradient_start, self.gradient_end)
        lmb.show()
        self.keys['lmb'] = lmb

        rmb = KeyWidget("RMB", self, mouse_w, mouse_h, show_cps=True, scale=scale,
                        animation_duration=self.animation_duration)
        rmb.move(rmb_x, mouse_y)
        rmb.set_global_opacity(self.opacity)
        rmb.set_gradient(self.gradient_start, self.gradient_end)
        rmb.show()
        self.keys['rmb'] = rmb

        self.repaint()
        QApplication.processEvents()

    def set_animation_duration(self, duration):
        self.animation_duration = duration
        for key in self.keys.values():
            key.animation_duration = duration

    def set_scale(self, scale):
        self.scale = scale
        self.create_keys(scale)
        self.update_gradient_colors()
        self.set_opacity(self.opacity)
        self.repaint()
        QApplication.processEvents()

    def set_opacity(self, op):
        self.opacity = op
        if not self.keys:
            return
        for key in self.keys.values():
            key.set_global_opacity(op)

    def update_gradient_colors(self):
        if not self.keys:
            return
        for key in self.keys.values():
            key.set_gradient(self.gradient_start, self.gradient_end)

    def on_key_pressed(self, key):
        if key in self.keys:
            self.keys[key].set_pressed(True)

    def on_key_released(self, key):
        if key in self.keys:
            self.keys[key].set_pressed(False)

    def on_mouse_pressed(self, btn):
        if btn == 'left':
            self.lmb_clicks.append(time.time())
            if 'lmb' in self.keys:
                self.keys['lmb'].set_pressed(True)
        elif btn == 'right':
            self.rmb_clicks.append(time.time())
            if 'rmb' in self.keys:
                self.keys['rmb'].set_pressed(True)

    def on_mouse_released(self, btn):
        if btn == 'left' and 'lmb' in self.keys:
            self.keys['lmb'].set_pressed(False)
        elif btn == 'right' and 'rmb' in self.keys:
            self.keys['rmb'].set_pressed(False)

    def update_cps_display(self):
        now = time.time()
        while self.lmb_clicks and self.lmb_clicks[0] < now - 1.0:
            self.lmb_clicks.popleft()
        while self.rmb_clicks and self.rmb_clicks[0] < now - 1.0:
            self.rmb_clicks.popleft()
        lmb_cps = len(self.lmb_clicks)
        rmb_cps = len(self.rmb_clicks)
        if 'lmb' in self.keys:
            self.keys['lmb'].set_cps(lmb_cps)
        if 'rmb' in self.keys:
            self.keys['rmb'].set_cps(rmb_cps)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos is not None:
            self.move(event.globalPos() - self.drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
        self.save_config()

    def create_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.create_tray_icon_pixmap())
        self.tray_icon.setToolTip("按键显示")

        tray_menu = QMenu()
        tray_menu.setStyleSheet("""
            QMenu {
                background-color: #f0f0f0;
                border: 1px solid #aaaaaa;
            }
            QMenu::item {
                padding: 5px 20px;
                color: #000000;
            }
            QMenu::item:selected {
                background-color: #aaaaaa;
                color: #000000;
            }
        """)

        settings_action = tray_menu.addAction("设置")
        settings_action.triggered.connect(self.open_settings)
        tray_menu.addSeparator()
        quit_action = tray_menu.addAction("退出")
        quit_action.triggered.connect(self.quit_app)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def create_tray_icon_pixmap(self):
        pixmap = QPixmap(64, 64)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor("#0F0C0F"))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(8, 8, 48, 48, 6, 6)
        painter.setPen(QColor(200,200,200))
        painter.setFont(QFont("Arial", 20))
        painter.drawText(pixmap.rect(), Qt.AlignCenter, "⌨")
        painter.end()
        return QIcon(pixmap)

    def open_settings(self):
        settings = SettingsDialog(self)
        settings.exec_()

    def load_config(self):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except Exception:
            return DEFAULT_CONFIG.copy()

    def save_config(self):
        config = {
            "opacity": self.opacity,
            "x": self.x(),
            "y": self.y(),
            "gradient_start": self.gradient_start.name(),
            "gradient_end": self.gradient_end.name(),
            "scale": self.scale,
            "animation_duration": self.animation_duration,
            "version": VERSION,
            "check_for_updates": self.config.get("check_for_updates", True),
            "ignored_version": self.config.get("ignored_version", "")
        }
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

    def quit_app(self):
        self.listener_thread.stop()
        self.listener_thread.wait()
        QApplication.quit()

    def closeEvent(self, event):
        self.save_config()
        self.listener_thread.stop()
        self.listener_thread.wait()
        event.accept()

    # ======================== 版本检测 ========================
    def check_for_updates(self):
        if not self.config.get("check_for_updates", True):
            return
        ignored = self.config.get("ignored_version", "")
        if ignored == VERSION:
            return
        self.update_thread = UpdateCheckThread()
        self.update_thread.finished.connect(self.on_update_finished)
        self.update_thread.error.connect(self.on_update_error)
        self.update_thread.start()

    def on_update_finished(self, remote_version):
        if remote_version != VERSION:
            # 使用 None 作为父窗口，避免继承主窗口透明背景
            msg = QMessageBox(None)
            msg.setWindowTitle("发现新版本")
            msg.setText(f"发现新版本：{remote_version}\n当前版本：{VERSION}\n是否更新？")
            msg.setIcon(QMessageBox.Information)
            # 自定义按钮
            update_btn = msg.addButton("更新", QMessageBox.AcceptRole)
            ignore_btn = msg.addButton("忽略", QMessageBox.RejectRole)
            ignore_perm_btn = msg.addButton("永久忽略", QMessageBox.DestructiveRole)
            msg.exec_()
            clicked = msg.clickedButton()
            if clicked == update_btn:
                webbrowser.open("https://github.com/bzm001/keystrokes/releases")
            elif clicked == ignore_perm_btn:
                self.config["ignored_version"] = VERSION
                self.save_config()

    def on_update_error(self, error_msg):
        # 判断是否超时，使用 None 作为父窗口
        if "timed out" in error_msg.lower() or "timeout" in error_msg.lower():
            QMessageBox.critical(None, "检查更新失败", "连接超时，请检查网络。")
        else:
            QMessageBox.critical(None, "检查更新失败", f"检查更新时发生错误：{error_msg}\n请检查网络或稍后再试。")

# ======================== 入口 ========================
def main():
    app = QApplication(sys.argv)
    # 设置程序图标（基于脚本所在目录）
    icon_path = os.path.join(BASE_DIR, "icon.ico")
    if not os.path.exists(icon_path):
        icon_path = os.path.join(BASE_DIR, "icon.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    app.setQuitOnLastWindowClosed(False)

    # 不再设置全局样式表，避免干扰 QMessageBox 等对话框

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()