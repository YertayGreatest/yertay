fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
for x in "banana":
  print(x)
#letters


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


for x in range(2, 6):
  print(x)
# 6 not included


for x in range(2, 30, 3):
  print(x)
#just add 3 to starting point, these will be steps

#------Nested Loops------
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


#if no content just write pass:
for x in [0, 1, 2]:
  pass
