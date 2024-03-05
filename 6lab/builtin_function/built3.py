s = input("string: ")
s.lower()
rev = s[::-1]
if rev == s:
    print("palindrome")
else:
    print("not")