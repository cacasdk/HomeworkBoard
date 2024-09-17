import os, datetime

class HomeworkBoard(object):
    def __init__(self, backup_dir='.\\backup\\',
                 template_name='template.docx',
                 homework='作业.docx',
                 desktop_path=os.environ.get('USERPROFILE')+'\\Desktop\\'):
        self.welcome()
        self.backup_dir = backup_dir
        self.template_name = template_name
        self.homework = homework
        self.desktop_path = desktop_path
        if self.today_used():
            if input('WARNING:today_used,do you want to OVERWRITE this?(y/N):') != 'y':
                exit(0)

    @staticmethod
    def welcome():
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
        print('Welcome to HomeworkBoard.')
    @staticmethod
    def success():
        print("Done!!!")
    def today_used(self):
        try:
            open(self.backup_dir + str(datetime.date.today()) + '.docx')
        except IOError:
            return False
        else:
            return True
    def make_backup(self):
        print('Creating backup...')
        try:
            homework=open(self.desktop_path +self.homework, 'rb')
            backup_file = open(self.backup_dir + str(datetime.date.today()) + '.docx', 'wb')
            backup_file.write(homework.read())
            homework.close()
            backup_file.close()
        except Exception as e:
            print(f'Error: {str(e)}')
            exit(1)
    def make_homework(self):
        print('Creating homework...')
        try:
            homework=open(self.desktop_path +self.homework, 'wb')
            template_file = open(self.template_name, 'rb')
            homework.write(template_file.read())
            homework.close()
            template_file.close()
        except Exception as e:
            print(f'Error: {str(e)}')
            exit(1)

