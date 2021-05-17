
box = {'color': 'red', 'age': 42}


for x in box.values():
    print(f"box.values() {x}")

for y in box.keys():
    print(f"box.keys() {y}")
#
# for z in box.items():
#     print(f"box.items() {z}")

# for a, b in box.items():
#     print(f"Key: {a} Value: {b}")

for k, v in box.items():
    print(f"Key: {k} Value: {v}")

print(55 in box.values())
print('color' in box.keys())



