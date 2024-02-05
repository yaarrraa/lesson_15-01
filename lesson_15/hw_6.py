my_dict = [{"name": "John", "age": 15},
           {"name": "Dan", "age": 73},
           {"name": "Pete", "age": 22},
           {"name": "Carlos", "age": 17},
           {"name": "Wesley", "age": 16},
           {"name": "Jameson", "age": 33},
           {"name": "Greyson", "age": 11},
           {"name": "Milo", "age": 77},
           {"name": "Harrison", "age": 61},
           {"name": "Dean", "age": 58},
           {"name": "Sutton", "age": 27},
           {"name": "Preston", "age": 69},
           {"name": "Tanner", "age": 22},
           {"name": "Sonny", "age": 11},
           {"name": "Archer", "age": 21},
           {"name": "Edward", "age": 34},
           {"name": "Braxton", "age": 49},
           {"name": "Jack", "age": 45}
           ]

ages = []
names = []
min_age_dict = []
max_name_dict = []
sum = 0
average_age = 0
for person in my_dict:
    value_1 = person.get("age")
    value_2 = person.get("name")
    ages.append(value_1)
    names.append(len(value_2))
min_age = (min(ages))
max_name = (max(names))
print(f"Minimal age = {min_age},\n"
      f"Maximum letters in name = {max_name}")

for person in my_dict:
    if person.get("age") == min_age:
        v_1 = person.get("name")
        min_age_dict.append(v_1)
    if len(person.get("name")) == max_name:
        v_2 = person.get("name")
        max_name_dict.append(v_2)
for value_ages in ages:
    sum += value_ages
print(f"List of the youngest persons = {min_age_dict}\n"
      f"List of people with the longest name = {max_name_dict}\n"
      f"Average age = {sum / len(ages)}")
