from random import randint
number_rand = randint(1, 10)
for i in range(1, 5):
    number_input = input('Enter a number from 1 to 10:')
    if int(number_input) < number_rand:
        print("The entered number is less than the specified one.")
    elif int(number_input) > number_rand:
        print("The entered number is greater than the one")
    else:
        print("You win!")
        break
else:
    print(f"You lost , the hidden number was: {number_rand}")