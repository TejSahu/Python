"""def build_tuple(*args):
    "Function to take multiple arguments"
    print(*args)
    return args


message = build_tuple("Hello", "from", "the", "other", "side")
print(type(message))
print(message)


def larsum(*args):
    "to find the largest and smallest of all"
    a = 1
    for i in range(len(args)):
        if a < args[i]:
            a = args[i]

    print("The largest of them all is:", a)
    for i in range(len(args)):
        if args[i] < a:
            a = args[i]
    print("The smallest of them is:", a)


larsum(3, 6, 4, 7, 1, 8, 23, 0)"""


# Average length of words passed as parameters
def words(*args):
    nwords = len(args)
    count = 0
    for a in range(nwords):
        count += len(args[a])
    avg = count // nwords
    print("Average length of words passed = ", avg)
    print(count)


# words("Hello", "him", "Avengers")

# list too can be packed and unpacked
def num(args):
    print(args)
    print(*args)


list1 = ['Amir', 'Chicken', 'Shop' , 'Lohegaon']
# num(list1)


# Reverse a string
def string_rev(args):
    args = args[len(args):: -1]
    print(args)


# string_rev("Nalasopara")

# Function to reverse list of arguments passed
def reverse(*args):
    for a in range(len(args)):
        print(args[a][::-1])


reverse("Hello", "Pillow")
