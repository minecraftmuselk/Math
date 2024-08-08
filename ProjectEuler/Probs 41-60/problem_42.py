"""Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?"""

file = open('words_42.txt', 'r')
f = file.read()

words = f.replace('"', '').split(',')

triangle_numbers = []
for i in range(1, 10_000):
    i = (i / 2) * (i + 1)
    i = int(i)
    triangle_numbers.append(i)


def get_word_value(word):
    d = dict()
    j = 1
    for i in range(ord('A'), ord('Z') + 1):
        d[chr(i)] = j
        j += 1
    word_value = 0
    word = word.upper()
    for letter in word:
        word_value += d[letter]
    return word_value


def is_triangle_word(word_value):
    for number in triangle_numbers:
        if word_value == number:
            return True
    return False


def main():
    triangle_words = 0
    for word in words:
        if is_triangle_word(get_word_value(word)):
            triangle_words += 1
    return triangle_words


print(words)
print(main())
