import datetime
import json
import os
import time

DEFAULT_SETTING = {
    "template_path": ".\\template.docx",
    "homework_path": "{0}\\Desktop\\homework.docx".format(os.environ['USERPROFILE']),
    "backup_dir": ".\\backup",
    "backup_suffix": ".docx"
}
SETTING_FILE_NAME = 'HomeworkBoard.setting.caca.json'


def output(word: str = '', end: str = '') -> str:
    """
    make SPECIAL output!!!
    :param word: the word you say
    :param end: the end part
    :return: word
    """
    for i in word:
        time.sleep(0.01)
        print(i, end='')
    print(end)
    return word


def welcome() -> None:
    """
    Welcome!!!
    :return:
    """
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
    output('Welcome to HomeworkBoard.')


def read_setting() -> dict:
    """
    Read setting file
    :return: setting
    """
    with open(SETTING_FILE_NAME, "r") as f:
        setting = json.loads(f.read())

    return setting


def write_setting(setting: dict) -> dict:
    """
    Read setting file
    :param setting: dict
    :return:
    """
    with open(SETTING_FILE_NAME, "w") as f:
        f.write(json.dumps(setting, sort_keys=True, indent=4, separators=(',', ': ')))
    return setting


def make_backup(homework: str, backup: str) -> bool:
    """
    Make backup file.
    :param homework: homework file
    :param backup: Backup file
    :return: success
    """
    success = False
    try:
        homework_file = open(homework, 'rb')
        backup_file = open(backup, 'wb')
        backup_file.write(homework_file.read())
        homework_file.close()
        backup_file.close()
    except Exception as e:
        print(e)
    else:
        success = True
    return success


def make_homework(homework: str, template: str) -> bool:
    """
    Make homework file.
    :param homework: homework file
    :param template: template file
    :return: success
    """
    success = False
    try:
        homework_file = open(homework, 'wb')
        template_file = open(template, 'rb')
        homework_file.write(template_file.read())
        homework_file.close()
        template_file.close()
    except Exception as e:
        print(e)
    else:
        success = True
    return success


def main():
    welcome()
    try:
        output('Reading setting file...')
        setting = read_setting()
    except FileNotFoundError:
        output('Hmm,maybe that\'s the first use\nInitialing setting file...')
        setting = write_setting(DEFAULT_SETTING)
    output('Making backup...')
    if not make_backup(setting['homework_path'],
                       setting['backup_dir'] + '\\{0}{1}'.format(datetime.date.today(), setting['backup_suffix'])):
        output('Oops,there is a mistake in make_backup')
        os.system('Pause')
        exit(1)
    if not make_homework(setting['homework_path'], setting['template_path']):
        output('Oops,there is a mistake in make_homework')
        os.system('Pause')
        exit(1)
    os.system('Pause')

if __name__=='__main__':
    main()