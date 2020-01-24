import string
rude_words_list = ["darn", "dammit", "stupid"]
sentence = "Darn, This is a rude Word. Dammit! I feel StuPID."
rude_words_count = 0
words = sentence.split(" ")
for word in words:
    print(f"original word: {word}")
    word = word.strip(string.punctuation).lower()
    print(f"reformed word: {word}")
    if word in rude_words_list:
        rude_words_count += 1
        print(f"Rude word found: {rude_words_count}. {word}")
print(f"\nTotal rude words found: {rude_words_count}")
if rude_words_count == 0:
    print("Congratulations! no rude words found.")
