data = {
    "apple": 50,
    "banana": 20,
    "orange": 35,
    "grape": 10
}

keys = list(data)

min_key = keys[0]
max_key = keys[0]

for key in data:
    if data[key] < data[min_key]:
        min_key = key
    elif data[key] > data[max_key]:
        max_key = key

print("Key with the smallest value:", min_key)
print("Smallest value:", data[min_key])

print("Key with the largest value:", max_key)
print("Largest value:", data[max_key])