for i in range(10, 100):
  print(i)

user_num = int(input("Please enter a number between 0 and 99: "))
if user_num == 0 or user_num <= 9:
  print("This is a single digit number")
elif user_num >= 10 and user_num <= 99:
  print("This is a double digit number")


