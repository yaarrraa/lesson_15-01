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

common_keys = []
only_keys_dict_1 = []

for key in my_dict_1.keys():
    if key in my_dict_2:
        common_keys.append(key)

for key in my_dict_1.keys():
    if key not in my_dict_2:
        only_keys_dict_1.append(key)

new_dict = {}

for key in my_dict_1.keys():
    if key not in my_dict_2:
        new_dict[key] = my_dict_1[key]

new_dict_2 = {}

for key in my_dict_1.keys():
    if key in my_dict_2:
        new_dict_2[key] = [my_dict_1[key], my_dict_2[key]]
    elif key not in my_dict_2:
        new_dict_2[key] = my_dict_1[key]

for key in my_dict_2.keys():
    if key not in my_dict_1:
        new_dict_2[key] = my_dict_2[key]

print(f"List of keys that are in both dictionaries = {common_keys} \n"
      f"List of keys that are in the first dictionary, but not in the second dictionary = {only_keys_dict_1} \n"
      f"New dictionary of pairs for keys that are in the first but not in the second dictionary = {new_dict} \n" 
      f"Combined new dictionary according to the rule = {new_dict_2}")
