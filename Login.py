'''
3. Регистрация и логин (консольный чат-бот). 
В программе есть список словарей, в каждом словаре два поля — логин и пароль. 
Мы можем дать чат-боту две три команды — выход, регистрация или логин. 
Если мы выбираем регистрацию, программа спрашивает логин и пароль, пароль два раза для надёжности. 
Если такой логин уже есть в списке — отказывает в регистрации. Если пароли два раза разные — отказывает в регистрации.
Если мы выбираем логин — просит ввести логин и пароль и проверяет, есть ли такая пара в списке логинов и паролей
'''
Peoples=[{"логин":"MarkovvvvvkaYT","пароль":"123qwe"}]
#Peoples={}
print("Здраствуйте, вы попали на сайт `горачие чебуреки`. Пожалуйста зарегестрируйтесь или войдите в своой аккаунт!")
Com=input("Введите команду: ")
while(Com!="Exit"):
    print()
    if Com=="Registration":
        Login=input("Придумайте логин✏: ")
        Password=input("Придумайте пароль✏: ")
        Password2=input("Повторите пароль✏: ")
        print()
        
        Nashli=False
        for user in Peoples:
            if user["логин"]==Login:
                Nashli=True
                print("Такой пользователь уже есть")
        
        
                
        while Password!=Password2 or Nashli!=False:
            if Password!=Password2:
                print("Не совпадают пароли!")
            elif Nashli==True:
                print("Такой пользователь уже есть, придумай другой логин!")
            
            Login=input("Придумайте логин✏: ")
            Password=input("Придумайте пароль✏: ")
            Password2=input("Повторите пароль✏: ")            
            for user in Peoples:
                if user["логин"]==Login:
                    Nashli=True
            
            '''
            elif Password!=Password2 or Nashli==True:
                print("Пролемы:")
                print("Такой пользователь уже есть, придумай другой логин!")
                print("Не совпадают пароли!")
            else:
                print("Пип пуп -_-, неизвестная ошибка!")
            '''
                
        Peoples.append({"логин":Login, "пароль":Password})
        print("Ура!")
        
        
    elif Com=="Login":
        Login=input("Введите логин✏: ")
        Password=input("Введите пароль✏: ")
        while not {"логин":Login,"пароль":Password} in Peoples:
            Login=input("Введите логин✏: ")
            Password=input("Введите пароль✏: ")
        print("Привет,",Login,"!")
    Com=input("Зарегестрируйтесь или войдите в свой аккаунт!: ")
