from HomeworkBoard import HomeworkBoard
import os

homework_board = HomeworkBoard()

if __name__=='__main__':
    homework_board.make_backup()
    homework_board.make_homework()
    os.system("Pause")