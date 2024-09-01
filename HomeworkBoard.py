import os
print(
    """
******************************************
   ******      **       ******      **    
  **////**    ****     **////**    ****   
 **    //    **//**   **    //    **//**  
/**         **  //** /**         **  //** 
/**        **********/**        **********
//**    **/**//////**//**    **/**//////**
 //****** /**     /** //****** /**     /**
  //////  //      //   //////  //      // 
******************************************
Welcome to CACA HomeworkBoard.
""")
print("Reading USERPROFILE... ", end='')
user_profile = os.environ['USERPROFILE']
print("\033[1;32mDone!\033[0m")
print("Reading template.docx... ", end='')
f1 = open("template.docx", "rb")
print("\033[1;32mDone!\033[0m")
print("Clearing 作业.docx... ", end='')
f2 = open(f"{user_profile}\\Desktop\\作业.docx", "wb")
print("\033[1;32mDone!\033[0m")
print("Copying template.docx to 作业.docx... ", end='')
f2.write(f1.read())
print("\033[1;32mDone!\033[0m")
"""print("Comparing template.docx and 作业.docx")
f2.close()
f3=open(f"{user_profile}\\Desktop\\作业.docx", "rb")
if f3.read() == f1.read():
    print("\\033[1;32mSUCCESSFULLY COPIED template.docx TO 作业.docx!!!\033[0m")
else:
    print("\033[1;31mFAILED!!!\033[0m")
    print("\033[1;31mPlease contact @Carrot729 on Github\033[0m")"""
print("Closing template.docx... ", end='')
f1.close()
print("\033[1;32mDone!\033[0m")
print("Closing 作业.docx... ", end='')
f3.close()
print("\033[1;32mDone!\033[0m")
os.system('Pause')