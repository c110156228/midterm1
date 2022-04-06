#判斷串列數字大小
n=[]

for i in range(10):
  n.append(eval(input()))
n.sort(reverse=True)
n.sort

print("最大的3個數字為:",n[0],n[1],n[2])
print("最小的3個數字為:",n[9],n[8],n[7])
