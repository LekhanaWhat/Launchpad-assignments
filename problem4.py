list1=[1,1,2,3,4,64,35,87,4,3]
print("the original list is:"+str(list1))
final=[]
for i in list1:
	if i not in final:
		final.append(i)
		print("The list after the duplicated elements are removed are:"+str(final))