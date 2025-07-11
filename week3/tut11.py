import re

data = ["hi123  ", "hello123  ", "hum  ", "dig345  "]

string = list(map(lambda s: re.findall(r'\d+', s), data))    # To display only digit
print(string)
string = list(map(lambda s: re.findall(r'\D+', s), data))   # To display only string, but if there is a digit in between then the string splits into two separate elements
print(string)
string = list(map(lambda s: re.sub(r'\D+', '', s), data))   # To replace the extra characters with empty string 
print(string)

string = list(map(lambda w: re.sub(r'^[aeiou](\w+)', w.upper(), w), data))   # capitalizes only first letters of every word
print(string)
string = list(map(lambda s: re.sub(r'\s+', ' ', s), data))
print(string)

email = ["a@gmail.com", "b@yahoo.com"]

dat = list(map(lambda s: re.search(r'@(\w+).', s).group(1), email))
print(dat)

