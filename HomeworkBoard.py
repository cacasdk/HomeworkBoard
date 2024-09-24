import os, datetime,time,json

def output(word: str = '', end: str = '') -> str:
    """
    make SPECIAL output!!!
    :param word: the word you say
    :param end: the end part
    :return: word
    """
    for i in word:
        time.sleep(0.01)
        print(i,end='')
    print(end)
    return word

DEFAULT_SETTING = {
    "template_path":".\\template.docx",
    "homework_path":"{0}\\Desktop\\homework.docx".format(os.environ['USERPROFILE']),
    "backup_path":".\\backup"
}
SETTING_FILE_NAME = 'HomeworkBoard.setting.caca.json'

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

def write_setting(setting:dict) -> None:
    """
    Read setting file
    :param setting: dict
    :return:
    """
    with open(SETTING_FILE_NAME, "r") as f:
        f.write(json.dumps(setting, sort_keys=True, indent=4, separators=(',', ': ')))
def make_backup(homework:str,backup:str) -> bool:
    """
    Make backup file.
    :param homework: homework file
    :param backup: Backup file
    :return: success
    """
    success=0
    try:
        homework_file=open(homework,'rb')
        backup_file=open(backup,'wb')
        backup_file.write(homework_file.read())
    except :

