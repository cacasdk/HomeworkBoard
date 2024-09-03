import os, datetime


class HomeWorkBoard:
    def __init__(self, backup_dir='.\\backup\\',
                 template_name='template.docx',
                 homework='作业.docx',
                 desktop_path=os.environ.get("USERPROFILE")+'\\Desktop\\'):
        self.welcome()
        self.backup_dir = backup_dir
        self.template_name = template_name
        self.homework = homework
        self.desktop_path = desktop_path
        self.homework_file_read = open(self.desktop_path + self.homework, 'rb')
        self.template_file = open(self.template_name, 'rb')
        self.backup_file = open(self.backup_dir + str(datetime.date.today()) + '.docx', 'wb')

    @staticmethod
    def success():
        print("\033[32mDone!!!\033[0m")

    def make_backup(self):
        try:
            print('Making backup... ')
            self.backup_file.write(self.homework_file_read.read())
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.success()

    def make_homework(self):
        self.homework_file = open(self.desktop_path + self.homework, 'wb')
        try:
            print('Making homework... ')
            self.homework_file.write(self.template_file.read())
        except Exception as e:
            print(e)
            exit(1)
        else:
            self.success()
        finally:
            self.homework_file.close()

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

    def __del__(self):
        self.backup_file.close()
        self.template_file.close()
        self.homework_file_read.close()

