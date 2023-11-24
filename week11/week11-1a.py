a = 30

ans = 0
for i in range(1, a+1):
  if a%i==0:
    print(i)
    ans += 1
print(a, '的因數個數有幾個', ans)