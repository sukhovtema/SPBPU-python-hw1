free_space = 1.44 * 2**20
book_pages_cnt = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_chars = 4

books_cnt = round(free_space / (book_pages_cnt * lines_per_page * chars_per_line * bytes_per_chars))

print("Количество книг, помещающихся на дискету:", books_cnt)