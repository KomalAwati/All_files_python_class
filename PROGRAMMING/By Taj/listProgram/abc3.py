# WAP to built a list with only the items having even number of character ?


names = ['amazon', 'gmail', 'yahoo', 'walmart', 'flipkart', 'rediff']
res = [ name  for name in names if len(name) % 2 == 0 ]

print(res)   #   ['amazon', 'flipkart', 'rediff']


