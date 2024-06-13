def upper_generator(x):
    for i in x:
        yield i.upper()

friuts=['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(friuts):
    print(i)