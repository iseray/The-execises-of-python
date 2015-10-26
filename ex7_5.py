import math

def jiecheng(x):
	a = 1
	for i in range(1,x+1):
		a = i * a
	return a
# print jiecheng(0)	

def estimate_pi():
	epsilon = math.pow(10, -15)
	k = 0
	sum = 0
	while True:
		item = jiecheng(4*k)*(1103 + 26390*k)/(math.pow(jiecheng(k),4) *math.pow(396,4*k))
		# print"the item is ", item
		sum = sum + item
		k += 1
		if item < epsilon:
			# print "The sum is ", sum, "The item is ", item
			break
		
	return 9801/(2 * math.sqrt(2) * sum) 

print "The estimate pi is ", estimate_pi(), "ok"
print "The exactly pi is ", math.pi


