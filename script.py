import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
# bookshelf is like [{}, {} , ...]
print("\n\n\n")


# comparison by title
def by_title_ascending(book_a, book_b):
    if book_a['title_lower'] > book_b['title_lower']:
        return True
    return False


# bubble sort 1  - 2 swaps
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# printing bubble sort1
for book in sort_1:
    print(book['title'])
print("\n\n\n")


# comparison by author name
def by_author_ascending(book_a, book_b):
    if book_a['author_lower'] > book_b['author_lower']:
        return True
    return False


# bubble sort 2 - 24 swaps
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

# printing bubble sort2
for book in sort_2:
    print(book['author'])
print("\n\n\n")
# quicksort
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

# printing quicksort1
for book in bookshelf_v2:
    print(book['author'])
print("\n\n\n")


# comparison by total length
def by_total_length(book_a, book_b):
    sum_a = len(book_a['title']) + len(book_a['author'])
    sum_b = len(book_b['title']) + len(book_b['author'])
    if sum_a > sum_b:
        return True
    return False


# loading book_large
long_bookshelf = utils.load_books("books_large.csv")
long_bookshelf_v1 = long_bookshelf.copy()
# bubblesorting large books
sorts.bubble_sort(long_bookshelf, by_total_length)

# printing sorted books
for book in long_bookshelf:
    print(book['author'])
print("\n\n\n")

# quicksorting large books
sorts.quicksort(long_bookshelf_v1, 0, len(long_bookshelf_v1) - 1, by_total_length)

# printing sorted books
for book in long_bookshelf_v1:
    print(book['author'])
print("\n\n\n")
