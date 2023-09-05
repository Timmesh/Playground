# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the character counts in both strings are equal
    return sorted(str1) == sorted(str2)

# Input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if they are anagrams
if are_anagrams(str1, str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
