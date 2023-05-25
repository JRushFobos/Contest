n = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list3 = []
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

x = ' '.join(str(x) for x in list3)

print(x)
