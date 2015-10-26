#coding:utf-8
#求取两个数的最大公约数

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)

print gcd(8,6)
print gcd(7,5)
