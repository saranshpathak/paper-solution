l=map(int,input().split())
b=list(l)
c=list()
for i in b:
	if i==0:
		c.append(i)
		b.remove(i)
b=b+c
print(b)
print(c)
