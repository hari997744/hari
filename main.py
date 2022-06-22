arr = [int(x) for x in input().split(',')]
k = int(input())
dic = {}
flag = 0
for i in arr:
  if (k-i) in dic:
    print('YES')
    flag = 1
    break
  else:
    dic[i]=1
if flag==0 :
  print('NO')