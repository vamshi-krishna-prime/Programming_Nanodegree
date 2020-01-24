# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > 
# profanity filter

# Rude words censorship, version 2
# Execute as 'python -u filename.py' for unbufferred/time delayed output

import string

rude_words = ["crap", "darn", "heck", "jerk",
              "idiot", "butt", "devil"]


def check_line(line):
    # split the line into individual words
    words = line.split(" ")
    new_words = []
    # check each word aganist rude words
    for word in words:
        # stripping punctuation and converting words into lower case
        new_word = word.lower().strip(string.punctuation)

        # if the word at the end of the line contain "\n", remove it
        if "\n" in new_word:
            new_word = new_word[0:len(new_word)-2]
        
        if new_word in rude_words:
            print(f"Rude word found: {new_word}")
            new_words.append("*" * len(new_word) + str(word[len(new_word):]))
        else:
            new_words.append(word)
    return (" ").join(new_words)


def check_file(original, censored):
    with open(original) as original_story:
        with open(censored, "w") as censored_story:
            # read one line at a time from my_file
            for line in original_story:
                # check each line for rude words
                new_line = check_line(line)
                censored_story.write(new_line)
            print("Censorship completed")
            print(f"Open '{censored}' for censored file")


if __name__ == '__main__':
    check_file("my_story.txt", "my_story_censored.txt")
