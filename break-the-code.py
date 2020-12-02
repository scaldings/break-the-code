import string


def get_words():
	words = []
	with open("words.txt", "r") as file:
		words = file.read().split("\n")
	return words


def filter_words(contains: str, words: list, can_repeat_letters: bool, word_length: int):
	valid_words = []
	for word in words:
		if contains != "":
			if contains in word:
				if len(word) == word_length:
					if can_repeat_letters == False:
						contained_letters = []
						for letter in word:
							if letter not in contained_letters:
								contained_letters.append(letter)
							else:
								pass
						valid_words.append(word)
					else:
						valid_words.append(word)
				else:
					pass
			else:
				pass
		else:
			if len(word) == word_length:
				if can_repeat_letters == False:
					contained_letters = []
					for letter in word:
						if letter not in contained_letters:
							contained_letters.append(letter)
						else:
							pass
					valid_words.append(word)
				else:
					valid_words.append(word)
			else:
				pass
	return valid_words


def double_letters():
	double_letters_list = []
	for letter in string.ascii_letters:
		double_letters_list.append(letter*2)
	return double_letters_list


def valid_words():
	valid = []
	valid_words4 = []
	for word in filter_words("", get_words(), True, 10):
		if word != "":
			if word[1] == word[4]:
				valid_words4.append(word)
	valid_words1 = []
	for double_letter in double_letters():
		for word in filter_words(double_letter, get_words(), True, 5):
			if word[1] == word[2]:
				valid_words1.append(word)
	valid_words3 = []
	for word in filter_words("",get_words(), False, 5):
		valid_words3.append(word)
	valid.append(valid_words1)
	valid.append(valid_words3)
	valid.append(valid_words4)
	return valid
	

def assemble():
	w1 = valid_words()[0]
	w3 = valid_words()[1]
	w4 = valid_words()[2]
	for word1 in w1:
		for word4 in w4:
			for word3 in w3:
				check = ((word3[0] not in 'aeiou') & (word1[4] == word4[8]) & (word4[1] == word4[4]) & (word3[3] == word4[7]) & (word3[4] == word4[9]))
				if check:
					print(f'{word1} a {word3} {word4}.')
					
						
if __name__ == "__main__":
	assemble()
