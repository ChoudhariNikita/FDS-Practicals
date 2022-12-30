def union(a,b):
	ans=a.copy()
	for i in b:
		if i not in a:
			ans.append(i)
	return ans 

# exclude intersection of a and b and only return set a
def minus(a,b):
	ans=[]
	for i in a:
		if i not in b:
			ans.append(i)
	return ans 

def intersection(a,b):
	ans=[]
	for i in a:
		if i in b:
			ans.append(i)
	return ans 

u=input("Enter roll no. of all students (Comma sepearated values):").split(",")
b=input("Enter roll no. of students who play badminton (Comma sepearated values):").split(",")
c=input("Enter roll no. of students who play cricket (Comma sepearated values):").split(",")
f=input("Enter roll no. of students who play football (Comma sepearated values):").split(",")

print("List of students who play both cricket and badminton",intersection(b,c))
result=union(minus(c,intersection(b,c)),minus(b,intersection(b,c)))
print("List of students who play either cricket or badminton but not both",result)
# print("List of students who play neither cricket nor badminton",minus(minus(u,b),c))
print("List of students who play neither cricket nor badminton",minus(u,union(c,b)))

print("Number of students who play cricket and football but not badminton",minus(intersection(c,f),b))
