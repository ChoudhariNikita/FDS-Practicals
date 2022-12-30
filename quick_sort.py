
def partition(per,lo,hi):
	if(lo<hi):
		pivot=lo # 1st element as pivot
		i=lo
		j=hi

		while(i<j):
			while(per[i]<=per[pivot] and i<hi):
				i=i+1
			while(per[j]>per[pivot]):
				j=j-1
			if(i<j):
				temp=per[i]
				per[i]=per[j]
				per[j]=temp

		temp=per[pivot]
		per[pivot]=per[j]
		per[j]=temp

		return j

def quicksort(per,lo,hi):
	# until low is less than high we are going to partition 
	if(lo<hi): 

		pi=partition(per,lo,hi) # returns proper position of pivot

		# when pivot element is at proper position
		# array is divided in two parts
		quicksort(per,lo,pi-1)
		quicksort(per,pi+1,hi)

per=[]

n= int(input("Enter the number of Students : "))
for i in range(n):
    m=float(input("Enter the percentage of Student {0} : ".format(i+1)))
    per.append(m)

print(per)

quicksort(per,0,n-1)  # pass 0th element and last element index

print("Sorted array :")
for i in range(n):
	print("%0.1f" % per[i])
print("Top 5 scores: ")
print(per[-5:n])

    
