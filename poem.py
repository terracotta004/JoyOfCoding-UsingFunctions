# poem.py
# Ben Underwood

# I have used str() unnecessarily in the past when getting user input.
# The input() function already returns a string, so wrapping it in str() is redundant.
# GitHub Copilot suggested removing the unnecessary str() calls as more Pythonic.

word1 = input("Enter first word (plural noun): ")

word2 = input("Enter second word (adjective): ")

print(word1.capitalize() + " are red, violets are blue")

print("Monty Python is " + word2.lower() + ", woo hoo!")
