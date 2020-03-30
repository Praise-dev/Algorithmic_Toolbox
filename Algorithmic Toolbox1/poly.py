# def multiply(A,B):
#     n = len(max(A, B))
#     product = []
#     for i in range (0, (2*n -1)):
#         product[i] = 0

#     for i in range (0, n-1):
#         for j in range(0, n-1):
#             product[i+j] += A[i] * B[j]
#     return product

# print(multiply([3,2,5], [5,1 ,2]))

# while(True):
#     for i in range(0, 10):
#         print(":)" * i)
#     break

#guess game
# from random import randint

# rand_num = randint(0, 10)
# def guess_game():
#     global rand_num
#     print(rand_num)
#     guess = int(input("what's your guess?"))
#     if guess > rand_num:
#         print("TOO HIGH!")
#         guess_game()
#     elif guess < rand_num:
#         print("TOO LOW")
#         guess_game()
#     else:
#         print("YOU WON!!")
#         play_again = input(" Dou you want to play again?? (y/n)")
#         if play_again == "y":
#             rand_num = randint(0, 10)
#             guess_game()
#         else:
#             print("bye")

# guess_game()

# playlist modelling
# playlist = [
#     {"title":"Again", "artist":"Wande Coal", "album":"WC", "year":"2020", "duration":"2:34" }
# ]

# for i in range(0,5):
#     playlist.append(dict.fromkeys(['title','artist','album','year','duration'], 'none'))

# print(playlist)

# Qwargs
# def US_states(**kwargs):
#     print(kwargs)
#     for states in kwargs.keys():
#         print(states)
#     return None

# US_states(TEXAS= 'DALLAS', ATLANTA='GEORGIA')

# Unpacking

# def sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# def names(**args):
#     for first, last in args.items():
#         print(f"{first} last name is {last}")
#     return None

# names(**{'praise': 'Okonta', 'James': 'Reece'})

# print(dict(praise='okonta', james='Reece'))

# BUILT-IN FUNCTIONS 
# filter
# name = ['Annie', 'Amaka', 'Becky', 'Henny', 'Timothy', 'bolaji']

# B_names = filter(lambda x: x.startswith(('B','b')), name)

# print(B_names)

# def rev(word):
#     for char in reversed(range(0, len(word))):
#         print(char)

# rev("Hello World")

# Decorators
# from functools import wraps
# def be_polite(fn):
#     @wraps(fn)
#     def wrapper():
#         print("What a pleasure to meet you")
#         fn()
#         print("Have a nice day")
#     return wrapper

# @be_polite
# def greet():
#     print("My name is Punchey")

# print(greet.__name__)


# # Generators
# def fib(n):
#     if n == 1:
#         return 1
#     for i in range(n):
#         yield (n-1) + (n-2)


# print(next(fib(2)))
# with open("./test.txt") as file:
#     print(file.read())
#     #file.write("123...123....12")
# print(file.closed)

# number = [1,2,3,4,5]
# print(number[:1:-1])
# from functools import wraps
# def number_format(fn):
#     @wraps(fn)
#     def wrapper(num):
#         numbers = fn([str(n) for n in num])
#         for i in range(len(numbers)):
#             standard = numbers[i][len(numbers[i])-10:] 
#             numbers[i] = "+91  " + standard[:len(standard)//2] + "  " + standard[len(standard)//2:]
#             print(numbers[i])     
#     return wrapper             
# @number_format
# def number_sort(num):
#     return sorted(num)

# if __name__ == "__main__":
#     l = [input() for _ in range(int(input()))]
#     number_sort(l)

# Working with CSV files


# # List of Strings to a String
# listOfStrings = ['One', 'Two', 'Three']
# strOfStrings = ''.join(listOfStrings)
# print(strOfStrings)

# # List Of Integers to a String
# listOfNumbers = [1, 2, 3]
# strOfNumbers = ''.join(str(n) for n in listOfNumbers)
# print(strOfNumbers)


# print(set([1,2,2,3,4,4,5,6,6,7,7,3,2]))

# helloWorld = ['hello','world','1','2']
# helloWorld.extend([3,4,5,6])

# Convert to a dictionary
# helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
# print(helloWorldDictionary)

# print(dict(zip(['hello', 1],['world',2])))

# print(['hello','world','1','2'].__iter__)

# print(helloWorld)


# list= ["23","22","098"]
# # print([[x,list.count(x)] for x in set(list)])

# a, b = list[:2]
# print(a)

# regex
# import re
# text = "Tales of the City (1998)"
# name = re.compile(r"(Mrs.|Mr.|Ms.) ([a-z]{2})[a-z]+", re.I)
# print(name.sub("\g<1> \g<2>****", text))

# rename = re.compile(r"(?P<title>[A-z\s]+) \((?P<year>\d{4})\)", re.M)
# # print(rename.findall(text))

# new = rename.sub("\g<year> - \g<title> ", text)
# print(len(new))

# for _ in new:
#     print("yo!")

# automate_the_boring_stuff_with_python exercise
# import re
# def re_strip(text, sub=None):
#     print(len(text))
#     if sub:
#         text = re.sub(sub, "", str(text))
#     else:
#         text = re.sub("^(\s)+ | (\s)+$", "", str(text))
#     print(len(text))
#     return text


# import re
# # libs = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
# def mad_libs(map):
#     with open("./test.txt", "r") as file:
#         line = file.readline()
#         words = ["ADJECTIVE", "NOUN", "VERB", "ADVERB"]
#         for word in words:
#             result = re.sub(word, map[word], line)
#             line = result  
#     return result

# if __name__ == '__main__':
#     print(""" 
#     input in the following sequence:
#     1. ADJECTIVE
#     2. NOUN
#     3. VERB
#     4. ADVERB
#     """)
#     keys = dict()
#     keys["ADJECTIVE"] = input("enter an ADJECTIVE ")
#     keys["NOUN"] = input("enter a NOUN ")
#     keys["VERB"] = input("enter a VERB ")
#     keys["ADVERB"] = input("enter an ADVERB ")
#     print(mad_libs(keys))



# def poly(A,B):
#     n=len(max(A,B))
#     product = [0 for _ in range((2*n) -1)]
#     for i in range(n):
#         for j in range(n):
#             product[i+j]+= A[i] * B[j]
#     return product

# print(poly([3,2,5],[5,1,2]))

# class Animal:

#     def  __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def __repr__(self):
#         return f"{self.name} is a {self.species}"

#     def make_sound(self, sound):
#         print(f"This animal makes the {sound} sound")

# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species = "cat")
#         self.breed = breed
#         self.toy =  toy


# Blue = Cat("Blue", "Scottish Fold", "ball")
# print(isinstance(Blue, Animal))

# class Aquatic:
#     def __init__(self, name):
#         self.name = name

#     def swim(self):
#         return f"{self.name} is swimming"

#     def greet(self):
#         return f"I am {self.name} of the sea!"

# class Ambulatory:
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         return f"{self.name} is walking"

#     def greet(self):
#         return f"I am {self.name} of the land!"

# class Penguin(Ambulatory, Aquatic):
#     def __init__(self,name):
#         super().__init__(name=name)


# captain_cook = Penguin("Captain Cook")

# class A:
#     def do_something(self):
#         print("Method Defined In: A")

# class B(A):
#     def do_something(self):
#         print("Method Defined In: B")

# class C(A):
#     def do_something(self):
#         print("Method Defined In: C")

# class D(B,C):
#     def do_something(self):
#         print("Method Defined In: D")

# thing = D()
# thing.do_something()

# print(help(D))
