strings = {}
string = input("Please enter a string: ").lower()
words = string.split()
for word in words:
    count = len(word)
    strings[word] = count + 1

words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print("{:{}}: {}".format(word, max_length, strings[word]))