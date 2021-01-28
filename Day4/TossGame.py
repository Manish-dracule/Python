import random
flag = True
while flag:
    print("Welcome to the Toss Game.\nTRY NOT TO LOSE TO A ROBOT.\n")
    res = input("Choose HEAD or TAIL: ")
    comp = random.randint(0,1)

    if res!= "HEAD" and res !="TAIL":
        print("Write Correctly you MORON!")
    elif comp == 0:
        print('HEADS COME.')
        print('-----\n| H |\n-----')
        if res == 'HEAD':
            print("YOU WIN.")
        else:
            print("YOU LOSE.")
    elif comp ==1: 
        print('TAILS COME.')
        print('-----\n| T |\n-----')
        if res == 'TAIL':
            print('YOU WIN.')
        else:
            print('YOU LOSE.')
    s = input('\nWanna Play Again?? enter 1 otherwise 0: ')
    if int(s)== 1:
        flag = True
    elif int(s)== 0:
        flag= False
    else:
        print("YOU ARE MORON, I am closing the game.")
        flag=False

    
    
