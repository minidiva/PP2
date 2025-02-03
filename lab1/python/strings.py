print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b = "Hello, World!" # The first char has index 0 
print(b[2:5]) # llo

b = "Hello, World!" # Leaving out the start index, range starts with 0
print(b[:5]) # Hello

b = "Hello, World!" # Leaving out the end index, range will go to the end
print(b[2:]) # llo, World!

b = "Hello, World!" # negative indexes to start the slice from the end (Inverted it starts from -1 at the end)
print(b[-5:-2]) # orl

a = "Hello, World!"
print(a.upper()) # HELLO, WORLD!

a = "Hello, World!"
print(a.lower()) # hello, world!

a = " Hello, World! " #remove whitespace from end and start
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J")) # Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

age = 36
txt = "My name is John, I am " + age
print(txt) # No formatting

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

price = 59
txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called "Vikings" from the north." #Not OK

txt = "We are the so-called \"Vikings\" from the north." #OK

