a = list(map(int, input().split() )) # 斷開, 整數, 變list

ans = a[0] # 取最前面的數字 a[0]
for x in a: # for迴圈, 把每個數字x巡過一遍
  if x>ans: # 如現在的x比ans還大
    ans = x # 離開迴圈時, 便找到ans
print('最大值是:', ans)

for x in a:
  print(x)