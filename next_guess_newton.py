x = float(input("What x to find the cube root of? "))
g = float(input("What guess to start with? "))
current_cube = g ** 3
print(f"Current estimate cube: {current_cube}")
next_guess = g - ((g ** 3 - x) / (3 * (g ** 2)))
print(f"Next guess: {next_guess}")