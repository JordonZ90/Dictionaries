box = {'name': 'Pooka', 'age': 5}

# if 'color' not in box:
#     box['color'] = 'black'

'''
setdefault is a way to do this with code
First argument passed to the method is the key to check for, and the second argument is the value to set at that key
if the key doesn't exist
'''

box.setdefault('color', 'black')

print(box.values())
print(box.keys())
