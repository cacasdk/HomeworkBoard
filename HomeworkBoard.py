import datetime
import json
import os
from pathlib import Path

# 默认配置设置，包括模板路径、作业路径和备份后缀
DEFAULT_CONFIG = {
    "template": f"{os.path.dirname(os.path.abspath(__file__))}\\template",
    "homework": f"{os.path.dirname(os.path.abspath(__file__))}\\homework",
    "backup": f"{os.path.dirname(os.path.abspath(__file__))}\\backup",
    "suffix": ".docx"
}
config = {}
# 设置文件名
CONFIG_FILE_NAME = 'config.json'


def welcome() -> None:
    """显示欢迎信息"""
    print('''
*************************************
 ######     ###     ######     ###    
##    ##   ## ##   ##    ##   ## ##   
##        ##   ##  ##        ##   ##  
##       ##     ## ##       ##     ## 
##       ######### ##       ######### 
##    ## ##     ## ##    ## ##     ## 
 ######  ##     ##  ######  ##     ## 
*************************************
    ''')
    print('Welcome to CacaHomeworkBoard.')


def read_config() -> dict:
    """读取设置文件"""
    config_path = Path(CONFIG_FILE_NAME)
    if not config_path.exists():
        return {}
    try:
        with open(config_path, "r", encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading config file: {e}")
        return {}


def write_config() -> None:
    """初始化设置文件"""
    try:
        with open(CONFIG_FILE_NAME, "w", encoding='utf-8') as f:
            json.dump(config, f, sort_keys=True, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error writing config file: {e}")
        exit(1)


def copy_file(src: Path, dst: Path) -> None:
    """
    拷贝函数
    :param src: Source file path
    :param dst: Destination file path
    """
    try:
        with open(src, 'rb') as src_file, open(dst, 'wb') as dst_file:
            dst_file.write(src_file.read())
    except FileNotFoundError:
        print(f"File not found: {src}")
        exit(1)
    except PermissionError:
        print(f"Permission denied: {src}")
        exit(1)
    except Exception as e:
        print(f"Error copying file: {e}")
        exit(1)


def make_backup() -> None:
    backup_dir = config['backup']

    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    backup_path = Path(backup_dir +'/'+ f'{timestamp}{config["suffix"]}')

    if backup_path.exists():
        print('Backup file already exists, do you want to overwrite it (y/N):', end='')
        if input().strip().lower() not in ['y', 'yes']:
            exit(0)

    copy_file(config["homework"]+config["suffix"], backup_path)


def make_homework() -> None:
    copy_file(config["template"]+config["suffix"], config["homework"]+config["suffix"])


def main():
    """主函数"""
    welcome()
    global config
    config = read_config()
    if not config:
        print("Config file not found. Use default configuration?")
        if input("Enter 'y' to use default configuration: ").strip().lower() == 'y':
            config = DEFAULT_CONFIG
            write_config()
        else:
            print("Exiting...")
            exit(0)

    make_backup()
    make_homework()


if __name__ == '__main__':
    main()
