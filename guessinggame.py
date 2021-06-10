import random
randomnum=random.randint(1,100)
print("Random number is  :", randomnum)
count=0
#randomnum=10
guess=int(input("Enter a guess  :"))
while(randomnum!=guess):
    count=count+1
    if guess<randomnum :
        guess=int(input("guess a higher number :"))
    else:
        guess=int(input("Guess a lower number :"))

print("your guess is right ", guess)
print("Number of guesses  ",count)
    
    
