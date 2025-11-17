import random
import string


def generate_and_guess_password(length):
    characters=string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range (length))
    print(f"The length of password is {length}, try to guess the password:")
    
    while True:
        guess = input("please enter your guess:")
        if len(guess) != length:
            print(f"The length must be {length},please enter again.")
        
        correct_position = 0
        for g, p in zip(guess,password):
            if g == p:
                correct_position += 1
        
        temp_password = list(password)
        temp_guess = list(guess)
        for i in range(length - 1, -1, -1):
            if temp_guess[i] == temp_password[i]:
                temp_guess.pop(i)
                temp_password.pop(i)
                
        correct_char = 0
        for g in temp_guess:
            if g in temp_password:
                correct_char += 1
                temp_password.remove(g)
                
        print(f"The number of charactors in the correct position is {correct_position}")
        print(f"the number of correct characters but the wrong position is {correct_char}")
        
        if correct_position == length:
            print("Congratulations, you guessed right!")
            return True
            
generate_and_guess_password(6)