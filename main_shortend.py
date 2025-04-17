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
    if((computer-you)==-1 and (computer-you)==2):
        print("you loose!")
    else:
        print("you win!")