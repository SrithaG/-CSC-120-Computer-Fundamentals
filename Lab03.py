number = int(input('Enter a number: '))
even_or_odd = number % 2
if even_or_odd > 0:
    print('This is an odd number')
else:
    print('This is an even number')

if number > 0 or number == 0:
    print("This is also a Positive number")
else:
    print("This is also a Negative number")

numbers = 40
print("The first 20 even numbers are: ")
for number in range(1, 41):
    if number % 2 == 0:
        print(number)
