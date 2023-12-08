a = int(input())
if a<2000:
	ans = 100
else:
	print( 100+(a-2000+499)//500 * 5 )