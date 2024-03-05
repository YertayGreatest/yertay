import os
path = os.getcwd()
filepath = "C:/Users/ASUS/Desktop/python projects/pythonUni/6lab/handling files/files1.py"
if os.path.exists(path):
    dis = os.path.splitext(os.path.basename(filepath))[0]
    print(dis)
else:
    print("Doesn't exist")
    
