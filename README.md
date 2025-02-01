# HomeworkBoard

## 简介

HomeworkBoard 是一个用于管理和刷新作业文档的 Python 工具。它可以帮助用户自动创建和备份家庭作业文件，确保每次使用时都是最新的模板。

## 功能特点

- 自动生成家庭作业文件。
- 自动备份旧的家庭作业文件。
- 支持配置文件自定义模板路径和作业路径。
- 提供日志记录功能，方便问题排查。

## 安装

### 环境依赖

确保已安装 Python 3.x 版本，并安装以下依赖库：
```shell
pip install -r requirements.txt
```

### 配置

首次运行程序时会自动生成默认配置文件 `HomeworkBoard.setting.caca.json`，您可以根据需要修改此文件中的配置项：
```json
{
    "backup_suffix": ".docx",  
    "homework_path": "C:\\Users\\XXX\\Desktop\\homework.docx", 
    "template_path": ".\\template.docx"
}
```
- `backup_suffix`: 备份文件后缀名，默认为 `.docx`。
- `homework_path`: 作业文件路径，默认为 `C:\\Users\\XXX\\Desktop\\homework.docx`。
- `template_path`: 模板文件路径，默认为 `.\\template.docx`。


## 使用方法

1. 将模板文件放置在配置文件中指定的 `template_path` 路径下。
2. 运行主程序 `HomeworkBoard.py`：
```shell
python HomeworkBoard.py
```
3. 程序将根据配置生成或更新家庭作业文件，并将其保存到 `homework_path` 指定的位置。
4. 旧的家庭作业文件会被备份到 `backup` 文件夹中，文件名格式为 `日期+backup_suffix`。

## 日志记录

程序运行时会在当前目录下生成日志文件 `HomeworkBoard.log.caca.txt`，记录程序执行过程中的信息和错误，便于后续调试和问题排查。

## 注意事项

- 在运行程序前，请确保关闭所有正在编辑的家庭作业文件（如 Word 文档），以免文件被占用导致操作失败。
- 如果需要覆盖当天已有的备份文件，程序会提示确认是否继续。

## 联系方式

如果您有任何问题或建议，请联系开发者。\
[Github](https://github.com/carrot729)|[Email](mailto:CarrotFrank@outlook.com)
---

感谢您使用 HomeworkBoard！希望这个工具能帮助您更高效地管理家庭作业。
