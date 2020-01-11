from time import sleep
from os import system
from random import randint

def lifecheck(ocean,i,j):
    count = 0
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if ocean[i][j] == ocean[k][l]:  count += 1
            
    return 3 <= count < 5 #посчитали на 1 больше



def borncheck(ocean,i,j):
    fishcount,shrimpcount = 0,0
    for k in range(i-1,i+2):
        for l in range(j-1,j+2):
            if ocean[k][l] == 2:
                fishcount += 1
            elif ocean[k][l] == 3:
                shrimpcount += 1

    if fishcount == 3:
        return 2
    elif shrimpcount == 3:
        return 3
    else:
        return False
            
def output(ocean):
    
    print(s2,(s0+s1)*(m-1),s0,s3,sep = '')
    print(s7,end = '')
    for j in range(1,m+1):
        print('{:^3d}'.format(ocean[1][j])+s7,end='')
    print()
    for i in range(2,n+1):
        print(s5,(s0+s4)*(m-1),s0,s6,sep='')
        print(s7,end='')
        for j in range(1,m+1):
            print('{:^3d}'.format(ocean[i][j])+s7,end='')
        print()

    print(s9+(s0+s8)*(m-1)+s0+s10)
            


def check(ocean,i,j):
    if ocean[i][j] == 1:
        pass
    elif ocean[i][j] == 0:
        ocean[i][j] = borncheck(ocean,i,j)
    else:
        ocean[i][j] = lifecheck(ocean,i,j)*ocean[i][j]

#Псевдографика
s0 = chr(9472)*3#горизонтальная палка
s1 = chr(9516)#лево право низ
s2 = chr(9484)#лев верхний угол
s3 = chr(9488)#прав верхн угол
s4 = chr(9532)#перекрестие
s5 = chr(9500)#верх низ право
s6 = chr(9508)#верх низ лево
s7 = chr(9474)#вертикальная палка
s8 = chr(9524)#лево право верх
s9 = chr(9492)#лев нижний угол
s10 = chr(9496)#прав нижний угол



while True:
    try:
        n,m = map(int,input('Введте размеры океана: ').split())
    except:
        print('Ошибка при вводе')
    else:
        break
key = int(input('Введите 1 для ручного заполнения, 0 для программного: '))
print(''' 0 - пустота
 1 - скала
 2 - рыба
 3 - креветка''')
if key:
    ocean = [[0]*(m+2)]
    print('Вводите элементы по одному через пробел по',m,'в одной строке')
    for i in range(n):
        ocean.append([0]+list(map(int,input().split()))+[0])
    ocean += [[0]*(m+2)]
else:
    ocean = [[0]*(n+2) for i in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            ocean[i][j] = randint(0,3)
output(ocean)
sleep(3)
system('cls')
oceancopy = ocean[:][:]
while True:
    print(''' 0 - пустота
 1 - скала
 2 - рыба
 3 - креветка''')
    for i in range(1,n+1):
        for j in range(1,m+1):
            check(ocean,i,j)
    output(ocean)
    sleep(3)
    system('cls')





    
