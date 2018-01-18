
First_list = ["12345", "12tef", "13dfs", "112rf", "12345"]
print(First_list)

print(First_list[1])

First_list.insert(1, "13dd3")
First_list.append("11r3t")

print(First_list)

for i in First_list:
    print(i + "1")
i = 0
while (i < len(First_list)):
    print("9?" + First_list[i])
    i = i + 1

A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = [11,12,13,14,15]
D = [16,17,18,19,20]
List = [A,B,C,D]

print(List[3][3])
for i in List:
    for j in i:
        if (j % 3 == 0):
            print(i,j)
"""Lololololll"""
def CompSquare(x, y):
    a = x*x - y*y
    b = 2 * x * y
    if (b == 0):
        print(a)
    elif (b < 0):
        print("{}{}i".format(a, b))
    else:
        print("{}+{}i".format(a, b))

CompSquare(3, -1)
CompSquare(-2, 0)
CompSquare(4, 5)