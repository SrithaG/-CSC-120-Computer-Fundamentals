user_string = int(input("Enter a binary string: "))
msb = int(str(user_string)[:1])
print("The Most Significant Bit is:", msb)

username = input("Please enter username: ")
if len(username) <= 6:
    print("Invalid Username. The length should be greater than 6 characters")
elif not username.islower():
    print("Invalid Username. Uppercase character found")
else:
    print("Valid Username")

i = 7
for j in range(1, 10):
    if j > i:
        print(j)

exponent = 0
# from 0 to 20
for i in range(0, 21):
    output = 2 ** exponent
    exponent = exponent + 1
    print(output)

for i in range(10, 50, 4):
    print(i * i)

a = 87
b = a % 7
print(b)
c = a / 7
print(c)
