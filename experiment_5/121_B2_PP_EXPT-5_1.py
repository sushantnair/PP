word = input("Enter a string: ")
#end=len(word)
def palindrome(start, end, word):
    if(word[start]==word[end] and start<end):
        palindrome(start+1, end-1, word)
    else:
        if(start>=end):
            print(word, " is a Palindrome.")
        elif(start<end):
            print(word, " is not a Palindrome.")
palindrome(0, len(word)-1, word)