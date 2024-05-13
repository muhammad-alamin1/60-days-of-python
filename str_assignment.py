word = input("Enter a word: ")

# Construct the new string with the word repeated and separated by hyphens
new_string = "-".join([word]*len(word))

print("Output:", new_string)  
