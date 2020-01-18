# Udacity > Intro to the Programming Nanodegree >
# Python part 2 > 3. Strings & Lists Part 2 > Section 19:
# Silly sentences

# Execute as 'python -u filename.py' for unbufferred/time delay output

# Random silly sentence
'''
Generate a random silly sentence using the supporting script of words
with verbs, nouns and templates in:
words.py
'''

# Instructions:
'''
1. Import random, time modules
2. Import suporting script (words.py)
3. Add a while loop that loops over the index position of the template.
4. Check if the slice that starts at the current position is '{{noun}}'.
If it is, append a random noun and advance the index position.
5. Use 'elif' to check if the slice that starts at the current position
is '{{verb}}'. If it is, append a random verb and advance the index position.
6. Otherwise (else) simply append the current character to the list.
7. Join the list to form a new string and return it.
'''


# Solution:


import random
import time
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index: index+8] == "{{noun}}":
            output.append(random.choice(nouns))
            index += 8
        elif template[index: index+8] == "{{verb}}":
            output.append(random.choice(verbs))
            index += 8
        else:
            output.append(template[index])
            index += 1

    # After the loop has finished, join the output and return it.
    output = "".join(output)
    return output


if __name__ == '__main__':
    while True:
        print(silly_string(words.nouns, words.verbs,
              words.templates))
        time.sleep(2)
