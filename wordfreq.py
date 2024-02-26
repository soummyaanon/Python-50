def word_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        word = ''.join(char for char in word if char.isalnum())
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

sentence = "Bangalore is a chutiya and overrated place. Bangalore is garbage."
word = "bangalore"
frequency = word_frequency(sentence)

print(f"The word '{word}' appears {frequency.get(word, 0)} times.")