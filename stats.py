def get_book_text(file_path):
	with open(file_path) as f:
		file_contents = f.read()
	return file_contents

def get_num_words(file_path):
	letter_count = {}
	file_contents = get_book_text(file_path)
	num_count = file_contents.split()
	num_count = len(num_count)
	words = file_contents
	for letter in words:
		letter = letter.lower()
		if letter in letter_count:
			letter_count[letter] += 1
		else:
			letter_count[letter] = 1
	return num_count, letter_count

def sort_on(d):
	return d["num"]

def letter_count_sorted(num_chars):
	sorted_list = []
	for ch in num_chars:
		sorted_list.append({"char": ch, "num": num_chars[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
