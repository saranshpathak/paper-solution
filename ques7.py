a=map(int,input().split(","))
b=list(a)
c=list()
d=b[-1]
e=b[0]
for i in range(e,d+1):
	if i not in b:
		c.append(i)
print(c)

