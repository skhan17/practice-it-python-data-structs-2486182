# palindromes practice
from collections import deque

def check_palindrome(word):
    # define deque
    d = deque(word)
    while len(d)>1:
        # if first and last letter do not match, its not a palindrome
        if d.pop() != d.popleft():
            return False
    return True

def main():
    #add code here
    # word = "choice"
    word = "tacocat"
    print(check_palindrome(word))

if __name__ == "__main__":
    main()