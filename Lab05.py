# Question 1
list1 = [0, 1, 2, 56, 77]
maximum_number = 0
for number in range(0, len(list1)):
    if number > maximum_number:
        maximum_number = number
print(list1[maximum_number])


# question 2

def create_list():
    import random
    max_len = 50
    my_list = []
    for i in range(max_len):
        my_list.append(random.randint(1, 99))
    return my_list


create_list()

# question 3
names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]
for i in range(len(names)):
    length = len(names[i])
    print("The length of the name", names[i], "is", length)

# question 4
names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]
for name in names:
    short_list = []
    for rest_of_names in names:
        if len(rest_of_names) <= len(name):
            short_list.append(rest_of_names)
        if name in short_list:
            short_list.remove(name)
    print("Names that are shorter in length or equal to", name, "are", len(short_list))
    print(short_list)

# question 5
names = ["Jennifer", "Albatross", "Justin", "Dave", "Shankarnarayan", "Ezra", "Alice", "Kwabena"]
i = 0
while i < (len(names)):
    short_list = []
    name = names[i]
    c = 0
    while c < (len(names)):
        if len(names[c]) <= len(names[i]):
            short_list.append(names[c])
        if name in short_list:
            short_list.remove(names[i])
        c = c + 1
    i = i + 1
    print("Names that are shorter in length or equal to", name, "are", len(short_list))
    print(short_list)

# question 6
import random

top_scores = []
for i in range(50):
    rand_num = random.randint(0, 100)
    print("New number generated: ", str(rand_num))
    top_scores.append(rand_num)
    if len(top_scores) > 5:
        top_scores.remove(rand_num)
        top_scores.insert(top_scores.index(min(top_scores)), rand_num)
        top_scores.remove(min(top_scores))

    print(top_scores)


# Extra Credit: Problem 1
# bubblesort
def main():
    sort_list = [1, 5, 78, 9, 4]
    print(bubblesort(sort_list))


def bubblesort(sort_list):
    for x in range(0, len(sort_list) - 1):
        for y in range(0, len(sort_list) - 1 - x):
            if sort_list[y] > sort_list[y + 1]:
                sort_list[y], sort_list[y + 1] = sort_list[y + 1], sort_list[y]
    return sort_list


main()
