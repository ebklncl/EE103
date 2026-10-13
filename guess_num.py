from secret_number import secretNum

guess = int(input("Guess the secret number: "))
attempt_count = 1  

while guess != secretNum:

    if attempt_count >= 5:
        while True:
            print("Oh! Noooooo...")
            
    if guess < secretNum:
        print("too low")
    else:
        print("too high")
        
    guess = int(input("Guess the secret number: "))
    attempt_count += 1

print("the same as the secret")