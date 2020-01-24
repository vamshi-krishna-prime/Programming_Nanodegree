# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > 
# profanity filter

# Rude words detector, version 1
# Execute as 'python -u filename.py' for unbufferred/time delayed output


rude_words = ["crap", "darn", "heck", "jerk",
              "idiot", "butt", "devil"]


with open("my_story.txt") as my_file:
    contents = my_file.read()
    rude_count = 0
    for rude in rude_words:
        if rude in contents:
            rude_count += 1
            print(f"Found rude word: {rude}")

if rude_count == 0:
    print("Congratulations, your file has no rude words.")
    print("At least, no rude words I know.")
else:
    print(f"Total rude words found: {rude_count}.")
