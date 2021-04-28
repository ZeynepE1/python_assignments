while True:
    number = input("enter a positive number:")
    digits = len(number)
    sum=0
    if not number.isdigit():
        print(number, "is invalid entry. enter numeric value!")
    elif int(number) >=0:
        for i in range(digits):
            sum = sum + int(number[i]) ** digits
        if sum == int(number):
            print(number,"is armstrong number.")
            break
        else:
            print(number, "is not armstrong number.")