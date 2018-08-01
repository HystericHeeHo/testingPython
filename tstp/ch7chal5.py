list1 = [8, 19, 148, 4]
list2 =[9, 1, 33, 83]
result = []

for item in list1:
    for item2 in list2:
        result.append(item * item2)  

print(result)