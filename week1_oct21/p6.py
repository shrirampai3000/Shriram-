#check if the input digit is composite number


number = int(input("Enter a positive integer greater than 1: "))

if number <= 1:
    print("Please enter a number greater than 1.")
elif number == 2:
    print(f"{number} is not a composite number (it is prime).")
else:
    if any(number % i == 0 for i in range(2, number)):
        print(f"{number} is a composite number.")
    else:
        print(f"{number} is not a composite number (it is prime).")
