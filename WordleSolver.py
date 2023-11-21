# Variables
wordlist = []      # List to store the words from the wordle dictionary
answer_List = []   # List to store possible words based on user input

# Load wordlist from file
with open("path to the wordlist") as w:
    wordlist = w.readlines()

# Main part of the program
while True:
    del answer_List[:]
    # Input
    letter = input("What letter do you know: ")   # User input for the known letter
    color = input("What color is the letter (y, g, b): ")   # User input for the color of the letter

    # If we got a green letter or yellow letter
    if color == 'g' or color == 'y':
        position = int(input("What position is the letter in (1 - 5): "))   # User input for the position of the letter
        position -= 1   # Adjust position to be zero-based

    # Go through all possible words
    for word in wordlist:
        # Green
        if color == 'g':
            if word[position] == letter:
                answer_List.append(word)
        # Black
        elif color == 'b':
            if letter not in word:
                answer_List.append(word)
        # Yellow
        elif color == 'y':
            if letter in word:
                if word[position] != letter:
                    answer_List.append(word)

    # Print out possible words
    wordlist = answer_List.copy()   # Update wordlist based on the narrowed down possibilities
    
    # Count the frequency of each letter in the remaining words
    letter_counts = {}
    for word in wordlist:
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

    # Find the most frequent letter
    max_count = 0
    best_guess = None
    for letter, count in letter_counts.items():
        if count > max_count:
            max_count = count
            best_guess = letter

    # Choose a word with the highest frequency of the most common letter
    for word in answer_List:
        if best_guess in word:
            print(word)
            break
