a = "Hello"
print(a)
#comment block of code:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

b = "Hello, World!"
print(b[-5:-2])
#result: orl

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

va = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#concatenate:
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#escape characters:
txt = "We are the so-called \"Vikings\" from the north."


