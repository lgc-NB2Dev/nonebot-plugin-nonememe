<!-- markdownlint-disable MD031 MD033 MD036 MD041 -->

<div align="center">

<a href="https://v2.nonebot.dev/store">
  <img src="https://raw.githubusercontent.com/NoneMeme/NoneMeme/main/static/favicon.png" width="180" height="180" alt="NoneBotPluginLogo">
</a>

<p>
  <img src="https://raw.githubusercontent.com/A-kirami/nonebot-plugin-template/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText">
</p>

# NoneBot-Plugin-NoneMeme

_✨ 看看 NoneBot 群大佬们的日常 ✨_

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
<a href="https://pdm.fming.dev">
  <img src="https://img.shields.io/badge/pdm-managed-blueviolet" alt="pdm-managed">
</a>
<a href="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/81ba4918-e38a-41dc-b7ab-8979dbc18578">
  <img src="https://wakatime.com/badge/user/b61b0f9a-f40b-4c82-bc51-0a75c67bfccf/project/81ba4918-e38a-41dc-b7ab-8979dbc18578.svg" alt="wakatime">
</a>

<br />

<a href="./LICENSE">
  <img src="https://img.shields.io/github/license/lgc-NB2Dev/nonebot-plugin-nonememe.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nonememe">
  <img src="https://img.shields.io/pypi/v/nonebot-plugin-nonememe.svg" alt="pypi">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nonememe">
  <img src="https://img.shields.io/pypi/dm/nonebot-plugin-nonememe" alt="pypi download">
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
吹水群：[1105946125](https://jq.qq.com/?_wv=1027&k=Z3n1MpEp)  
邮箱：<lgc2333@126.com>

## 💡 鸣谢

### [NoneMeme](https://nonememe.icu/)

- 梗图来源

## 💰 赞助

感谢大家的赞助！你们的赞助将是我继续创作的动力！

- [爱发电](https://afdian.net/@lgc2333)
- <details>
    <summary>赞助二维码（点击展开）</summary>

  ![讨饭](https://raw.githubusercontent.com/lgc2333/ShigureBotMenu/master/src/imgs/sponsor.png)

  </details>

## 📝 更新日志

### 0.2.0

- 自动更新图片列表
- 缓存获取到的图片和图片列表

### 0.1.1

- 发送梗图会回复指令消息
