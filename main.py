import random
print("Who are you?")
name=input("> ")
print("Hello, John!")
print("Tossing a coin...")
head=0
tail=0
for i in range(3):
    print("Round "+str(i+1)+": ",end="")
    num = random.random()
    num*=100
    num=num//10
    if num%2 == 1:
        print("Tail")
        tail+=1
    else:
        print("Head")
        head+=1

print(f"Heads: {head},Tails: {tail}")
if head > tail:
    print(f"You won!")
else:
    print(f"You lost!")
