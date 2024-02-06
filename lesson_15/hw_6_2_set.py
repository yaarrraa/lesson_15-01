my_dict_1 = {1: 1,
             2: 2,
             3: 3,
             4: 4,
             5: 5,
             "name": "Sutton",
             "age": 22,
             }
my_dict_2 = {"name": "Dan",
             "age": 17,
             4: 4,
             2: 2,
             "city": "Kyiv",
             3: 1,
             }

keys_1 = set(my_dict_1.keys())
keys_2 = set(my_dict_2.keys())

both_dict = list(keys_1.intersection(keys_2))

only_first_dict = list(keys_1.difference(keys_2))

new_d = {}
for key in only_first_dict:
    new_d[key] = my_dict_1[key]

new_dict = {}
for key in only_first_dict:
    new_dict[key] = my_dict_1[key]

for key in list(keys_2.difference(keys_1)):
    new_dict[key] = my_dict_2[key]

for key in both_dict:
    new_dict[key] = [my_dict_1[key], my_dict_2[key]]

print(f"List of keys that are in both dictionaries = {both_dict}\n"
      f"List of keys that are in the first dictionary, but not in the second dictionary = {only_first_dict} \n"
      f"New dictionary of pairs for keys that are in the first but not in the second dictionary = {new_d} \n"
      f"Combined new dictionary according to the rule = {new_dict}")
