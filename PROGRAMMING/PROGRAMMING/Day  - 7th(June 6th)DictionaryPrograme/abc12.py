
#6. Creating Dictionary of city and population pairs using Dict Comprehension

cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]
population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]
d = { city: population for city, population in zip(cities, population) }

print(d)

#  {'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778',
#         'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}
