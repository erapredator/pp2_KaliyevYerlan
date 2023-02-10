# Write a function that accepts string from user, return a sentence with the words reversed
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

sentence = input("Enter a sentence: ")
print(reverse_sentence(sentence))