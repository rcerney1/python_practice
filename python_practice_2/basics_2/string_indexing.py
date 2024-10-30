#string indexing = accessing elements of sequence using []
#                  [start : end : step]

credit_number = "1234-5678-9012-3456"

first_number = credit_number[0]
first_four_digits = credit_number[0:4]
second_four_digits = credit_number[5:9]
last_twelve_digits = credit_number[5:]
last_number = credit_number[-1]

all_even_numbers = credit_number[1::2]
reversed_number = credit_number[::-1]
print(first_four_digits, second_four_digits, last_twelve_digits, last_number, all_even_numbers, reversed_number)