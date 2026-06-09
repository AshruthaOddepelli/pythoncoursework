data={
    'subbu':{'status':True,'python':98,'Mqsql':95,'flask':94},
    'nagendra':{'status':True,'python':78,'Mqsql':65,'flask':84},
    'dinesh':{'status':False,'python':None,'Mqsql':None,'flask':None},
    'ashu':{'status':True,'python':68,'Mqsql':55,'flask':64},
    'rishi':{'status':True,'python':33,'Mqsql':25,'flask':34},
    }
name=input("enter the name:")

if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['Mqsql']+data[name]['flask']
        avg=total/3
        if avg>90:
            print(f"congrats {name}, you got first in class!!!")
        elif avg >70:
            print(f"Good {name}, keep it up for the next time!!")
        elif avg>35:
            print(f"Better{name}, work hard next time!")
        else:
            print(f"{name} , you have failed in the exam.Bring your parents")
    else:
        print(f"{name} didn't write the exam .Bring your parents")
else:
    print(f"{name}'s data is not found")
                  
    
