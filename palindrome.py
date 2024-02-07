def isPalindrome(word):
    if word == "":
        return True
    elif word[0] != word[-1]:
        return False
    return isPalindrome(word[1:-1])

print (isPalindrome("madam"))