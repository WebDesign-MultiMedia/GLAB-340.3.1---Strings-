# Word play game

word = input("Enter a word: ") # Get a word from the user

#Lenght of the word
print("Length of the word is: ", len(word)) # Print the length of the word

#Uppercase and lowercase of the word
print("Uppercase:", word.upper()) # Print the word in uppercase
print("Lowercase:", word.lower()) # Print the word in lowercase

# Counting occurrences of a letter in the word
letter = input("Enter a Letter: ") # Get a letter from the user
print(f"'{letter}' appears {word.count(letter)} time(s) in '{word}'") # Print the number of times the letter appears in the word

substring = input("Enter a substring: ") # Get a substring from the user
print(f"'{substring}' appears {word.count(substring)} time(s) in '{word}'") # Print the number of times the substring appears in the word

#Reversing the word
reverse_word = word[::-1] # Reverse the word
print("Reverse:", reverse_word) # Print the reversed word

#Slicing the word
start_index =  int(input("Enter the starting index: "))
end_index = int(input("Enter an ending index: "))
sliced_word = word[start_index:end_index]
print("Sliced word:", sliced_word) # Print the sliced word

#Replacing a  character
char_to_replace = input("Enter a character to replace: ")
replacement_char = input("Enter a character to replace with: ")
new_word = word.replace(char_to_replace, replacement_char, 1)
print("Replaced:", new_word) # Print the new word

#Checking for plaindrome and valid indentifier
is_plaindrome = word == reverse_word # Check if the word is a palindrome
is_valid_indentifier = word.isidentifier() # Check if the word is a valid identifier

print("Is a palindrome:", is_plaindrome) # Print if the word is a palindrome
print("Is a valid Python indetiifer:", is_valid_indentifier) # Print if the word is a valid Python identifier