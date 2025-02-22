import re

with open("row.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 1
def match_a_b(text):
    return re.search(r"ab*", text) is not None 

# 2
def match_a_b2or3(text):
    return re.search(r"\bab{2,3}\b", text) is not None 

# 3
def find_underscore_sequences(text):
    return re.findall(r"[a-z]+_[a-z]+", text)

# 4
def findOneUppercaseLetterThenlowercase(text):
    return re.findall(r"[A-Z][a-z]+", text)

# 5
def match_a_anything_b(text):
    return re.search(r"a.*b$", text) is not None

# 6
def replace_special_chars(text):
    return re.sub(r"[ ,.!]", ":", text)

# 7
def snake_to_camel(snake_str):
    return re.sub(r'_([a-zA-Z])', lambda match: match.group(1).upper(), snake_str)

# 8 
def split_at_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)

# 9 
def insert_spaces(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)

# 10
def camel_to_snake(camel_str):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_str).replace('__', '_').lower()

# 1 
print('11111111111111111111111111111111111111',match_a_b(text))

# 2
print('\n2222222222222222222222222222222222222', match_a_b2or3(text))

# 3
print('\n333333333333333333333333333333333333', find_underscore_sequences(text))

# 4
print('\n44444444444444444444444444444444444444', findOneUppercaseLetterThenlowercase(text))

# 5
print('\n55555555555555555555555555555555555555555555', match_a_anything_b(text))

# 6 
print('\n666666666666666666666666666666666666666', replace_special_chars(text))

# 7 
print('\n77777777777777777777777777777777777777777', snake_to_camel(text))

# 8
print('\n88888888888888888888888888888888888888888', split_at_uppercase(text))

# 9
print('\n9999999999999999999999999999999999999', insert_spaces(text))

# 10
print('\n1000000000000000000000000000000000000', camel_to_snake(text))