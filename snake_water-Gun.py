import random
'''
s for snake
w for water
g for gun
'''
computer= random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict ={1:"Snake", -1:"water",0:"Gun"}
you =youDict[youstr]

#By now we have 2 var (you and Computer)
print(f"You Choose {reverseDict[you]}\n Computer Choose {reverseDict[computer]}")

if (computer == you):
    print("Its a Draw")
else:
    if (computer == -1 and you ==1):
        print("you Win! ")
    elif (computer == -1 and you ==0):
        print("you Lose! ")
    elif (computer == 1 and you ==-1):
        print("you lose! ")
    elif (computer == 1 and you ==0):
        print("you Win! ")
    elif (computer == 0 and you ==-1):
        print("you Win! ")
    elif (computer == 0 and you ==1):
        print("you lose! ")
    else:
        print("Something Went Wrong ")
        
        