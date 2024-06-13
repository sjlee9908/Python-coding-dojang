x={'a':10, 'b':20, 'c':30, 'd':40}

for key, value in x.items():
    if value==20:
        del x[key]

print(x)
