# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

first_string = set("zxcvb21")
second_string = set("qwertyz1")
print(first_string & second_string)
# or
print(first_string.intersection(second_string))
# or
s = first_string & second_string
print("\n".join(s))


