import random
'''
s = 1
w = -1
g = 0
'''
computer=random.choice([1,-1,0])
youstr=input("Enter your choice : ")
youdic={"s":1,"w":-1,"g":0}
you=youdic[youstr]
reverse_str={1:"snake",-1:"water",0:"gun"}


print(f"Computer choose {reverse_str[computer] }\nYou choose {reverse_str[you]} ")

if(computer==you):
    print("It's a draw!")
else:
    if(computer==-1 and you==1): #-2
        print("you win!")
    elif(computer==-1 and you==0): #-1
        print("you loose!")
    elif(computer==1 and you==-1): #2
        print("you loose!")
    elif(computer==1 and you==0): #1
        print("you win!")
    elif(computer==0 and you==1):#-1
        print("you loose!")
    elif(computer==0 and you==-1):#1
        print("you win!")
    else:
        print("something went wrong!")



