# Question 6
SCORES = [40, 91, 85, 15]
SCORES2 = SCORES[:]
pairs = []
for x in SCORES:
    for y in SCORES2:
        if x != y:
            if (y, x) not in pairs:
                pairs.append((x, y))
                print(str(x) + "," + str(y))

# Extra Credit Challenge Question
s = "i_love_programming_in_python_and_i_will_alzways_program"

char_noted = {}
for char in s:
    if char in char_noted:
        char_noted[char] = char_noted[char] + 1
    else:
        char_noted[char] = 1

unique_characters = []
for char in char_noted:
    if char_noted[char] == 1:
        unique_characters.append(char)
print('The unique characters in this string are:', unique_characters)
