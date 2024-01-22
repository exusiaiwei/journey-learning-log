# import
import random

# define of dice faces
valid_faces = [4, 6, 8, 10, 12, 20]
dice_faces = int(input("Please choose the number of faces on the dice (4,6,8,10,12,20) :"))

while dice_faces not in valid_faces:
    print('Invalid input. Please choose the number of faces on the dice (4,6,8,10,12,20) :')
    dice_faces = int(input("Please choose the number of faces on the dice (4,6,8,10,12,20) :"))
print('You have chosen a dice with' , dice_faces, 'faces.')

# roll the dice
times = int(input("How many times do you want to roll :"))
print('You would like to roll the dice' , times ,'times')

# initialize the total
total = 0
# roll the dice
for _ in range(times): #The _ is used as a loop variable to indicate that this variable is not actually used in the loop body.
    dice_result = random.randint(1, dice_faces)
    total += dice_result
print('The total points rolled is' , total)





