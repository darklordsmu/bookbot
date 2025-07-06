import sys

from stats import get_book_text, get_num_words, letter_count_sorted


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words, letter_dict = get_num_words(book_path)
	sorted_list = letter_count_sorted(letter_dict)
	print_report(book_path, num_words, sorted_list)

def print_report(book_path, num_words, sorted_list):
	print("============ BOOKBOT  ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

main()
	
