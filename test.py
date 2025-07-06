def letter_count(words):
	letters = {}
	words = words.split()
	for word in words:
		word = word.lower()
		for letter in word:
			if letter in letters:
				letters[letter] += 1
			else:
				letters[letter] = 1
def sort_on(s):
	return s("num")

def sorted_list(chars_dict):
	sorted_list = []
	for ch in chars_dict:
		sorted_list.append({"char": ch, "num": chars_dict[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	print(sorted_list)
letter_count("Test Words")
