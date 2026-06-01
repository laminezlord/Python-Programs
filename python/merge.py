list1 = ["py", "is", "awes"]
list2 = ["thon", "", "ome"]

def merge(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

print(merge(list1, list2))