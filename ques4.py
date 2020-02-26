a=map(int,input().split(","))
l1=list(a)
c=50
h=30
for i in l1:
	q=(((2*c*i)/h)**0.5)
	p=int(q)
	print(p,end=",")
	
