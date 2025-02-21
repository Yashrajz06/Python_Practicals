# 3. Write the program to sort a dictionary in ascending or descending order by key and
#     ascending or descending by value.

dicts = {
"Virat": 50,
"Rohit": 50,
"Rahul": 50,
"Shubhman": 50,
"Jadeja": 50,
"Suresh": 50,
"Ashwin": 50,
"Hardik": 50,
}

print(sorted(dicts.items(), key=lambda x: x[0]))
print(sorted(dicts.items(), key=lambda x: x[1]))
