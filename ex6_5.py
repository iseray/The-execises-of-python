#coding:utf-8


import sys   
sys.setrecursionlimit(1000000) #例如这里设置为一百万(set maximum recrusion depth)
def ack(m, n):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	else:
		return ack(m-1, ack(m, n-1))


print ack(3,4)
print ack(4,1)
