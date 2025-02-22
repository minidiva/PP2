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



# 1 task tests

print("\nTask 1 tests:")
print(match_a_b("a"), "a")
print(match_a_b("ab"), "ab")
print(match_a_b("abb"), "abb")
print(match_a_b("abbb"), "abbb")
print(match_a_b("abbbbbbbbbb"), "abbbbbbbbbb")
print(match_a_b("zombie"), "zombie")

# 2 task tests
print("\nTask 2 tests:")
print(match_a_b2or3("abbb"), "abbb")
print(match_a_b2or3("abb"), "abb")
print(match_a_b2or3("abbbbbbbb"), "abbbbbbbb")

# 3 task tests
print("\nTask 3 tests")
print(find_underscore_sequences("stringthathave_underscore"))
print(find_underscore_sequences("stringThatDon't"))

# 4 task tests
print("\nTask 4 tests")
print(findOneUppercaseLetterThenlowercase("Nusdhfufu"))
print(findOneUppercaseLetterThenlowercase("asjdsjad"))

# 6 task tests
print("\nTask 6 tests")
print("Wow,This is really interesting! -> ", replace_special_chars("Wow,This is really interesting!"))

# 7 task tests
print("\nTask 7 tests")
print("how_i_did_that -> ", snake_to_camel("how_i_did_that"))
print("snake_to_camel -> ", snake_to_camel("snake_to_camel"))

# 8 task tests
print("\nTask 8 tests")
print("HelloWorldExample -> ", split_at_uppercase("HelloWorldExample"))  

# 9 task tests
print("\nTask 9 tests")
print("HelloWorldExample -> ", insert_spaces("HelloWorldExample")) 

# 10 task tests
print("\nTask 10 tests")
print("SnakeToCamel -> ", camel_to_snake("SnakeToCamel"))
print("HowIDidThat -> ", camel_to_snake("HowIDidThat"))
