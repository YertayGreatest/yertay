def palindrome(word):
    rev = word[::-1]
    if rev == word:
        print("word is palindrome")
    else:
        print("word is NOT palindrome")