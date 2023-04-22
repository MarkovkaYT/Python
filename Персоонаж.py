#import playsound

'''
Лист заданий «Словари»
1. Консольная программа-«чат-бот», которая всё время спрашивает команду. В программе есть словарь, описы
вающий персонажа с 6ю свойствами. По определённой команде можно добавить персонажу новые свойства, параметры, осо
бенности, или переделать существующие. По другой команде можно вывести всю информацию о персонаже.
'''
Persoonazh={}
print("Дарова, ты супер, гипер, пупер, турбо, ой короче какой то левый, а может и правый носок.\nНо сейчас не об этом! Ты должен создать свой ботинок, ой то есть персоонажа. \nСделай ему одежду, разум и 0 iq.")
print("")
("Для этого используй команды!")

Com=input("Передай ботинку команду: ")
while(True):
    print()
    
    if Com=="Add":
        if len(Persoonazh)<10 or len(Persoonazh)==10:
            ArgName=input("Введи имя новой части: ")
            ArgIn=input("Добавь что будет в новой части ботинка: ")
            Persoonazh[ArgName]=ArgIn
        else:
            print("Ботинок не может вместить в себя больше 10 деталей")
    elif Com=="Set":
        ArgName=input("Измени часть своего ботинка, но сначала введи имя его части: ")
        isExist=False
        for key in Persoonazh:
            if key ==ArgName:
                isExist=True
                break
        
        if isExist==True:
            ArgIn=input("Изменяй часть ботинка: ")
            Persoonazh[ArgName]=ArgIn
        else:
            print("У ботинка нету такой части, но ты можешь сделать её с помощью команды Add!")
        
        
    elif Com=="Del":
        ArgName=input("Введи имя части которую хотите удалить: ")
        del Persoonazh[ArgName]
    elif Com=="Print":
        print(Persoonazh.keys())
        print(Persoonazh.values())
    elif Com=="Exit":
        exit()
    else:
        print("Ты дал ботинку не правильную команду '_'")
        print("")
    Com=input("Передай ботинку команду: ")
