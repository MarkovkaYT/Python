pers = {
    " ": "15 ", 
    "суперспособность": "умеет летать "
    
    }
   
   

for key in pers:
    print(key,':', pers[key])

print("команды: добавить заменить уйти команды вывод ")
comanda = input("введите команду")
while comanda != "уйти":
    if comanda == "добавить":
        add = input("напишите что хотели бы добавить")
        znac = input("значение")
        pers[add] = znac
        for key in pers:
            print(key,':', pers[key])
    
    
    elif comanda == "заменить":
        zamena = input("заменить ключ")
        pip = input("значение к ключу")
        pers[zamena] = pip
        for key in pers:
            print(key,':', pers[key])
    
    comanda = input("введите команду")   
