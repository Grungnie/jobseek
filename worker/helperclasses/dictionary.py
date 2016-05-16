import re


class Dictionary:
    def __init__(self):
        self.dictionary_location = 'worker/helperclasses/words.txt'

        # Read in dictionary
        temp_dict = list(line.lower().strip()
                         for line in open(self.dictionary_location))

        # Remove all words less than 3 characters (performance)
        #temp_dict = [s for s in temp_dict if len(s) > 2]

        self.dictionary = set()
        for word in temp_dict:
            self.dictionary.add(self.clean_word(word))

    # Dictionary Analysis
    def count_words(self, word_stats):
        word_count = 0
        for word in word_stats:
            word_count += word['count']

        return word_count

    def check_for_word(self, word, strip_special=True):
        word = word.strip()
        word = word.lower()

        if word in self.dictionary:
            return True
        else:
            return False

    def return_words(self, text_sample):
        words = []
        words_temp = {}
        word_count = 0

        text_sample = text_sample.lower().split()

        for word in text_sample:
            if len(word) > 2:
                if self.check_for_word(word):
                    if word in words_temp:
                        words_temp[word] += 1
                    else:
                        words_temp[word] = 1

                    word_count += 1

        for word, value in words_temp.items():
            percentage = value / word_count * 100
            words.append({'value': word, 'count': value, 'percentage': percentage})

        return words

    def clean_word(self, word):
        word = re.sub("^[^a-zA-Z]", '', word)
        word = re.sub("[^a-zA-Z]$", '', word)
        return word.lower()

    def clean_string(self, string_to_clean):
        # split words
        word_list = []
        temp_word_list = string_to_clean.lower().split()

        # remove leading and trailing spaces
        for index in range(len(temp_word_list)):
            word = temp_word_list[index]

            word = re.sub("^[^a-zA-Z]", '', word)
            word = re.sub("[^a-zA-Z]$", '', word)

            # check if word exists
            if self.check_for_word(word):
                word_list.append(word)
            else:
                # Check for combinations of 2 words
                words_found = False
                for letter_index in range(len(word)-1, 0, -1):
                    if (self.check_for_word(word[:letter_index]) and self.check_for_word(word[letter_index:])):

                        word_list.append(word[:letter_index])
                        word_list.append(word[letter_index:])
                        words_found = True
                        break

                if not words_found:
                    # Find largest possinle word
                    for letter_index in range(len(word), 2, -1):
                        if self.check_for_word(word[:letter_index]):
                            word_list.append(word[:letter_index])
                            break

        return ' '.join(word_list)