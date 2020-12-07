#take a string and print the reverse of the string
#this is done by taking the length of the word, n, and printing the nth postion
#the while loop will print this position, then iterates to the n-1 th postion and continues to do this till 0th position

word = input("Please enter your string to be reversed:")

def inverter(word):
    pos = len(word)
    while pos >= 0:
        print(word[pos])
        pos -= 1