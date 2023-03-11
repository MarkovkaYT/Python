def Pallindrom(A):
    for index in range(len(A)//2):
        if A[index] != A[-index-1]:
            return False
    return True


def Pallindrom2(A,index):
    if index > len(A)/2:
        return("Это паллиндром! ")
        
    elif A[index] != A[-index-1]:
        return("Это не паллиндром! ")
    else:
        return (Pallindrom2(A,index+1))
    
        
 
A=input("Пиши чё хочешь: " )
print(Pallindrom2(A,0))
    