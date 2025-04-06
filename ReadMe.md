# 离线英语词典

这是一个基于Python开发的英语词典查询与发音工具，集成了本地词典查询和单词TTS发音功能。
这个项目的灵感基于[Flint](https://github.com/sh0ckj0ckey/Flint)项目。
数据库源源自[ECDICT](https://github.com/skywind3000/ECDICT)
因为C#看不懂，所以用了python自己写了个小工具，原理不太难。
代码开发主要用时2天，嗯，基本都是AI写的。

## 版本
- 0.0.1 
  - 总之能用了，嗯
  - 支持单词tts发音
  - 查询的单词tts发音
  - 输入即查询

## 功能特性

- 📖 本地词典查询：支持精确查询和模糊匹配
- 🔊 TTS发音：支持单词和查询结果离线TTS发音
- 🖥️ 图形界面：简洁易用的GUI界面
- 🚀 快速响应：本地数据库查询，响应迅速

## 依赖环境

- Python 3.8+
- pyttsx3
- tkinter

## 安装与使用

目前建议克隆/下载仓库，然后只要运行main.py即可
有兴趣的开发这可以自现删减，自行编译

## 项目结构

    tts/
    ├── python/
    │   ├── main.py              # 主程序
    │   ├── UI.py                # 图形界面
    │   ├── tts.py               # TTS发音模块
    │   ├── dict_process.py      # 词典处理模块
    │   └── ECDICT/              # 词典文件夹
            └──stardict.db          # 词典数据库

debug.py只是个调试用文件，可以不管它。
现在只是测试了下使用free dictionary的api获取单词发音，不过效果不太理想。获取释义是没啥问题的。

## 待解决问题：
- 软件部署与安装包
- 单词发音中数字的发音问题
- 更多释义，尤其是英文释义
- 更多扩展功能
  - 单词本？
  - 更多UI设置
  - 在线单词原声发音
  - 离线音标发音