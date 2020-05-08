#    3. A palindrome is a sentence that contains the same sequence of letters reading
#       it either forwards or backwards. A classic example is 'Able was I, ere
#       I saw Elba.." Write a recursive function that detects whether a string is a
#       palindrome. The basic idea is to check that the first and last letters of the
#       string are the same letter; if they are, then the entire string is a palindrome
#       if everything between those letters is a palindrome.
#         There are a couple of special cases to check for. If either the first or
#        last character of the string is not a letter, you can check to see if the rest
#        of the string is a palindrome with that character removed. Also, when you
#        compare letters, make sure that you do it in a case-insensitive way.
#          Use your function in a program that prompts a user for a phrase and
#        then tells whether or not it is a palindrome. Here's another classic for
#        testing: "A man, a plan, a canal, Panama!"


def palindrome(xStr, firstRun = True):
    if firstRun == True:
        for ch in '<}{ ][>.?/:;\|+=-_),(*&^%$#@!~`':
            xStr.replace(ch, "")
        xStr = xStr.lower()

    if len(xStr) < 2:
        return  True
    elif xStr[0] == xStr[-1]:
        xStr = xStr[1: -1]
        palindrome(xStr, firstRun = False)
        return True
    else:
        return False

def main():
    xSrt = input("Type a phrase to check for palindrome status here: ")
    if palindrome(xSrt) is True:
        print("The phrase is a palindrome.")
    else:
        print("The phrase is not a palindrome.")

main()

# I started from cleaning the sentence first by removing the punctuations and lowercasing it.
# If the sentence contains only one letter, it counts as a palindrome. If more than two letters,
# and the first and last letters are the same, it is also a palindrome. Otherwise, it's not.
