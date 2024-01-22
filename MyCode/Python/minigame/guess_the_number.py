# import
import random
# variables
number = random.randint(1,100)
running = True

# control flow
while running:
    guess = int(input('Please input your guess')) #must put guess variable here or it will cause infinate loop
    print("Your guess is:" , guess)
    if guess == number:
        print('You win!')
        print('But no reward!')
        running = False
    elif guess > number:
        print('Lower!')
    else:
        print('Higher!')
# end
print('End')