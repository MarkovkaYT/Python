import random
def generate():
    num1=random.randint(1,9)
    num2=random.randint(0,9)
    while num1==num2:
        num1=random.randint(1,9)
        num2=random.randint(0,9)
    num3=random.randint(0,9)
    while num2==num3 or num3==num1:
        num3=random.randint(0,9)
    print(num1,num2,num3)
    
    return str(num1)+str(num2)+str(num3) 

def equals(str1, str2):
    if str1==str2:
        return True
    else:
        return False
        
    

A=0
Zagadano = generate()
Razgagano=input("Разгадай число: ")
if  equals(Zagadano,Razgagano):
    print("Молодец!!!")
else:
    print("Ты не угадал!")
    
print("Загадали: ", Zagadano)
