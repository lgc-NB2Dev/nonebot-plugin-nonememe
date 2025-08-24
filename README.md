<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/NoneMeme/NoneMeme/main/static/favicon.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/plugin.svg" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-NoneMeme

_✨ 看看 NoneBot 群大佬们的日常 ✨_

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/uv">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/81ba4918-e38a-41dc-b7ab-8979dbc18578">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/81ba4918-e38a-41dc-b7ab-8979dbc18578.svg" alt="wakatime">
</a>

<br />

<a href="https://pydantic.dev">
  <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/template/pyd-v1-or-v2.json" alt="Pydantic Version 1 Or 2" >
</a>
<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-nonememe.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nonememe">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-nonememe.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nonememe">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-nonememe" alt="pypi download">
</a>

<br />

<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-nonememe:nonebot_plugin_nonememe">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin%2Fnonebot-plugin-nonememe" alt="NoneBot Registry">
</a>
<a href="https://registry.nonebot.dev/plugin/nonebot-plugin-nonememe:nonebot_plugin_nonememe">
  <img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fnbbdg.lgc2333.top%2Fplugin-adapters%2Fnonebot-plugin-nonememe" alt="Supported Adapters">
</a>

</div>

## 📖 介绍

### 我好菜啊

![我好菜啊](https://raw.githubusercontent.com/lgc-NB2Dev/readme/main/nonememe/intro.png)

## 💿 安装

以下提到的方法 任选**其一** 即可

<details open>
<summary>[推荐] 使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```bash
nb plugin install nonebot-plugin-nonememe
```

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```bash
pip install nonebot-plugin-nonememe
```

</details>
<details>
<summary>pdm</summary>

```bash
pdm add nonebot-plugin-nonememe
```

</details>
<details>
<summary>poetry</summary>

```bash
poetry add nonebot-plugin-nonememe
```

</details>
<details>
<summary>conda</summary>

```bash
conda install nonebot-plugin-nonememe
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分的 `plugins` 项里追加写入

```toml
[tool.nonebot]
plugins = [
    # ...
    "nonebot_plugin_nonememe"
]
```

</details>

## ⚙️ 配置

[config.py](./nonebot_plugin_nonememe/config.py)

## 🎉 使用

指令：`nonememe` / `nb草图` / `nb梗图`  
不带参数则随机选取一个，带上参数可以进行搜索，参数使用 `/` 开头及结尾使用正则表达式搜索

### 效果图

如果有效果图的话

## 📞 联系

QQ：3076823485  
Telegram：[@lgc2333](https://t.me/lgc2333)  
吹水群：[168603371](https://qm.qq.com/q/EikuZ5sP4G)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [NoneMeme](https://nonememe.icu/)

- 梗图来源

## 💰 赞助

**[赞助我](https://blog.lgc2333.top/donate)**

感谢大家的赞助！你们的赞助将是我继续创作的动力！

## 📝 更新日志

### 0.3.1

- 兼容 HTTPX 0.28

### 0.3.0

- 适配 Pydantic V1 & V2
- 换用 alconna

### 0.2.0

- 自动更新图片列表
- 缓存获取到的图片和图片列表

### 0.1.1

- 发送梗图会回复指令消息
