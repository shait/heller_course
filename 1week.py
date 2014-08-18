import random

print("я загадал число от 0 до 100, попробуй его угадать!")

min_number = 0
max_number = 100

guessedNumber = random.randint(min_number, max_number)

while guessedNumber != "":
    userNumber = int(input("введи число"))
    if (userNumber < 0) or (userNumber > 100):
        print("введи число от 0 до 100:")
        continue
    if userNumber < guessedNumber:
        print("загаданное число больше введеного!")
        continue
    if userNumber > guessedNumber:
        print("загаднное число меньше введеного")
        continue
    if userNumber == guessedNumber:
        print("бинго ты угадал!")
        break
input()

