# Keystrokes

[![Release](https://img.shields.io/badge/Release-1.0.0-blue.svg)](https://github.com/bzm001/keystrokes/releases)
[![Python](https://img.shields.io/badge/Python-3.12-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Keystrokes** 是一款专为游戏玩家设计的按键显示工具，支持显示键盘按键（WASD、Space、Shift）和鼠标按键（LMB/RMB），并提供实时 CPS（点击次数/秒）显示。界面简洁、透明、可自定义位置、透明度、颜色渐变和动画效果。

---

## ✨ 特性

- **实时按键显示**：WASD、Space、Shift 按键按下/松开状态可视化。
- **鼠标 CPS 检测**：左键（LMB）和右键（RMB）的 CPS 实时显示。
- **高度自定义**：
  - 调节整体不透明度。
  - 自定义字体渐变色（起始/结束颜色）。
  - 调整窗口位置（拖动或设置坐标）。
  - 按键大小缩放（0.5x ~ 2.0x）。
  - 动画时长（按压/松开淡入淡出速度）。
- **视觉反馈**：
  - 按下时按键不透明度增加 25%，并显示彩色渐变边框（平滑淡入淡出）。
  - 松开时边框平滑消失。
- **系统托盘**：右键托盘图标快速打开设置或退出程序。
- **配置持久化**：所有设置自动保存至 `keystrokes_config.json`，支持版本升级检测。
- **跨版本升级**：配置文件版本校验，自动修复无效值。

---

## 📦 下载与安装

### 方式一：直接运行可执行文件（推荐）
1. 前往 [Releases](https://github.com/bzm001/keystrokes/releases) 下载最新版本的 `Keystrokes.exe`。
2. 双击运行，程序将常驻系统托盘。

### 方式二：从源码运行
1. 确保已安装 **Python 3.12**（更高版本可能不兼容）。
2. 克隆仓库：
   ```bash
   git clone https://github.com/bzm001/keystrokes.git
   cd keystrokes

安装依赖：

```bash
pip install PyQt5 pynput
```

安装完成后运行：
```bash
python main.py
```

方式三：自行打包（可选）
项目提供了打包脚本，需安装 PyInstaller：

```bash
pip install pyinstaller
```

然后运行打包脚本：

build312.bat（快速打包）

build312-2.bat（详细打包，含依赖检查）

打包后生成 dist/Keystrokes.exe。

---

🖱️ 使用方法
移动窗口：按住窗口任意空白区域拖动。

打开设置：右键系统托盘图标（⌨） → 选择“设置”。

退出程序：右键系统托盘图标 → 选择“退出”。

设置界面说明

 选项 -----|----- 说明

不透明度 | 按键背景的透明度（10%~100%），按下时会额外增加 25%。

字体渐变 | 按键文字的起始颜色和结束颜色（线性渐变）。

窗口位置 | X、Y 坐标（像素），超出屏幕范围会自动修正。

按键大小 | 整体缩放比例（50%~200%），所有按键等比例缩放。

动画时长 | 按键按下/松开时背景和边框的淡入淡出时间（0~0.5 秒）。

---

⚙️ 配置文件

首次运行后，会在同目录生成 keystrokes_config.json，内容示例如下：

```json
{
  "opacity": 0.5,
  "x": 0,
  "y": 800,
  "gradient_start": "#ff0000",
  "gradient_end": "#ffff00",
  "scale": 0.75,
  "animation_duration": 0.05,
  "version": "Release-1.0.0"
}
```

opacity：背景不透明度（0~1）。

x / y：窗口左上角坐标（整数）。

gradient_start / gradient_end：字体渐变色（十六进制颜色值）。

scale：按键大小缩放（0.1~1.0）。

animation_duration：动画时长（秒，0~0.5）。

version：当前配置文件版本（自动维护）。

程序启动时会自动检查配置文件完整性，修正无效值，并支持版本升级提示。

---

📝 版本历史

Release-1.0.0 (2026-08-06)
Release-1.0.1 (2026-08-06)

完整更新日志请查看源码头部注释。

---

🤝 贡献

欢迎提交 Issue 和 Pull Request。如果你发现任何问题或建议，请通过 Issues 反馈。

---

📄 许可证

本项目采用 MIT 许可证，详情见 LICENSE 文件。
