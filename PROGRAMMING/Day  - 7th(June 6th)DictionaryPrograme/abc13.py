
# 7. Create a dictionary of dialcode and country from the following list

dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
# 1
d = {}

for code, country in dial_codes:
    if code not in d:
        d[code] = country

# print(d)

# 2
dc = { item[0]: item[-1]  for item in dial_codes}
# print(dc)

# 3
dc2 = { code: country    for code, country in dial_codes }
print(dc2)

# {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia',
#     55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria',
#        7: 'Russia', 81: 'Japan'}
