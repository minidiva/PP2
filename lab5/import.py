import regex.py

with open("row.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1 
print(regex.match_a_b(text))

# 2
print(regex.match_a_b2or3(text))

# 3
print('\n', find_underscore_sequences(text))

# 4
print('\n', findOneUppercaseLetterThenlowercase(text))

# 5
print('\n', match_a_anything_b(text))

# 6 
print('\n', replace_special_chars(text))

# 7 
print('\n', snake_to_camel(text))

# 8
print('\n', split_at_uppercase(text))

# 9
print('\n', insert_spaces(text))

# 10
print('\n', camel_to_snake(text))

