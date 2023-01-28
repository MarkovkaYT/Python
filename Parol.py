def numcheck(parol): 
    nums_here=False
    for sym in parol:
        if sym > "0" and sym < "9":
            nums_here=True
            break
    return nums_here
def mineBykvi(parol): 
    buk_here=False
    for buk in parol:
        if buk > "a" and buk < "z":
            buk_here=True
            break
    return buk_here
def mineBykvi(parol): 
    buk_here=False
    for buk in parol:
        if buk > "a" and buk < "z":
            buk_here=True
            break
    return buk_here
def BigBykvi(parol): 
    buk_here=False
    for buk in parol:
        if buk > "A" and buk < "Z":
            buk_here=True
            break
    return buk_here
def six(parol): 
    buk_here=False
    for buk in parol:
        if len(parol) > 5:
            buk_here=True
            break
    return buk_here
def simvol(parol):
    Simvols=["!","%","_","-","+","?","*","@","&","~","#","(",")",",","`","/","\\","|","$","№",";"]
    
    simvol_here=False
    for simvol in parol:
        if simvol in Simvols:
            simvol_here=True
            break
    return simvol_here
            



parol=input("Придумай пароль: ")
if not numcheck(parol):
    print("ТВОЙ ПАРОЛЬ БЕЗ цИфЕрОк!!!")
if not mineBykvi(parol):
    print("ТВОЙ ПАРОЛЬ БЕЗ МАЛЕНЬКИХ БуКоВоК!!!")
if not BigBykvi(parol):
    print("ТВОЙ ПАРОЛЬ БЕЗ БОЛЬШИХ БуКоВоК!!!")
if not six(parol):
    print("ТВОЙ ПАРОЛЬ МЕНЬШЕ ЧЕМ 6 сИмВоЛоВ!!!")
if not simvol(parol):
    print("ТВОЙ ПАРОЛЬ БЕЗ СпЕцИАлЬНыХ СиМвОлОв!!!")
    
    
    
