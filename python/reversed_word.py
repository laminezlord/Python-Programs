word = input("Enter a word: ")
reversed_word = ""
for i in range(len(word)):
    reversed_word += word[len(word) - 1 - i]
print("Reversed word:", reversed_word)

if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")