#    prints vowel name

names = ["steve", "eve", "alex", "john", "alexa"]
vowles = lambda name: name[0].lower() in "aeiou"
print(list(filter(vowles, names)))


#   output:-   ['eve', 'alex', 'alexa']