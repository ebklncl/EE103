# while True:    
#     given_number = int(input("Enter an integer number: "))
#     if given_number < 0:
#     print("Square root of negative numbers is not a real number.")
#     else:
#     guess_number = 1
#         while guess_number * guess_number < given_number:
#         guess_number += 1
#         if guess_number * guess_number == given_number:
#         print(f"The square root of {given_number} is {guess_number}")
#         else:
#         print(f"{given_number} is not a perfect square.")
# # print("-" * 30)

# 
while True:
    given_number = int(input("Enter an integer number (or enter 0 to exit): "))
    
    if given_number == 0:
        print("Exiting program. Goodbye!")
        break

    is_negative = False
    if given_number < 0:
        is_negative = True
        working_number = -given_number
    else:
        working_number = given_number

    guess_number = 0
    
    while guess_number * guess_number * guess_number < working_number:
        guess_number += 1
        
    if guess_number * guess_number * guess_number == working_number:
        if is_negative:
            guess_number = -guess_number
        print(f"The cube root of {given_number} is {guess_number}")
    else:
        print(f"{given_number} is not a perfect cube.")
            
    print("-" * 30)