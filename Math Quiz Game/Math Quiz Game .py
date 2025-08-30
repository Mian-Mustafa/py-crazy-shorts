import random , time

score = 0
for i in range (5):
    a, b = random.randint(1,10),random.randint(1,10)
    ans = int(input(f"{a}+{b} = "))
    if ans == a+b:
        print("✅ Correct!")
        score +=1
    else:
        print("❌ Wrong !")
        
print("your Score :" ,score ,"/5")