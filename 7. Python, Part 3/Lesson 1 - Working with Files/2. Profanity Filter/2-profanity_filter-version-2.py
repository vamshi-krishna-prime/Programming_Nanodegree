# Udacity > Intro to the Programming Nanodegree >
# Python part 3 > 1. Working with Files > 
# profanity filter

# Rude words detector, version 2
# Execute as 'python -u filename.py' for unbufferred/time delayed output


rude_words = ["crap", "darn", "heck", "jerk",
              "idiot", "butt", "devil"]


def check_line(line):
    rude_count = 0
    # split the line into individual words
    words = line.split(" ")
    # check each word aganist rude words
    for word in words:
        if word in rude_words:
            rude_count += 1
            print(f"Found a rude word: {word}")
    return rude_count


def check_file(filename):
    with open(filename) as my_file:
        rude_count = 0
        # read one line at a time from my_file
        for line in my_file:
            # check each line for rude words
            rude_count += check_line(line)
        
        if rude_count == 0:
            print("Congratulations, your file has no rude words.")
            print("At least, no rude words I know.")
        else:
            print(f"Total rude words found: {rude_count}")


if __name__ == '__main__':
    check_file("my_story.txt")
