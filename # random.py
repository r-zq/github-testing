# random
import random
random.seed(345)


random.seed(213)
guess = None
count = 0
while guess != random.randint(0,5):
    count += 1
    guess = int(input('guess the number: '))
    
print (f'congrats, you got the correct number: {guess}')
print (f'number of guesses: {count}')
    