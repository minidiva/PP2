import random

def ounceToGram(n):
    return n * 28.3495231

# print(ounceToGram(50))

def fahrenheitToCelsium(n):
    return (5/9) * (n-32)

# print(fahrenheitToCelsium(50))

def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2

    chickens = numheads - rabbits

    a = [rabbits, chickens]
    return a

# a = 34
# b = 94
# print('[Rabbits, Chickens] = ' , solve(a, b))

def filter(a):
    list = []
    for x in a:
        if(x % 2 == 0):
            list.append(x)
    return list

# print(filter([1,5,7,8,3,4]))

def permute(s, answer):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)

# input = input()
# print("All permutations of the string are: ")
# permute(input, "")

def reverse(string):
    return string[::-1]

# print(reverse("We are ready"))

def has_33(nums):
    i = 0
    while i + 1 < len(nums):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        else:
            i += 1
    return False

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))

def spy_game(nums):
    a = []
    for x in nums:
        if x == 0 or x == 7:
            a.append(x)
    if a[0:3] == [0,0,7]:
        return True
    else:
        return False
        
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

def volume(radius):
    return 1/3 * 3.14 * radius

# print(volume(13))

def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

# original_list = [1, 2, 2, 3, 4, 4, 5]
# print(unique_elements(original_list))

def is_palindrome(s):
    s = s.lower()
    s = s.replace(",", "")
    s = s.replace(" ", "")
    s = s.replace(".", "")
    return s == s[::-1]

# print(is_palindrome("No lemon, no melon"))

def histogram(list):
    for x in list:
        print('*' * x)

# histogram([4,5,3])

def guessTheNumber():
    answer = random.randint(1,20)
    attempts = 0


    name = str(input("Hello! What is your name? \n"))
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    game_is_over = False
    while(game_is_over != True):
        guess = int(input())
        if guess < answer:
            print('\n')
            print("Your guess is too low.")
            print("Take a guess.")
            attempts += 1
            continue
        elif guess > answer:
            print('\n')
            print("Your guess is to high")
            print("Take a guess.")
            attempts += 1
            continue
        else:
            print(f"Good job, {name}! You guessed my number in {attempts+1} guesses!")
            return 0
        
# guessTheNumber()