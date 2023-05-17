from buscar import Find

def Delete(array, num):
	find=Find(array, num)
	for i in range(len(find)):
		array[find[i]]=''
		if find[i]==0:
			array=array[1:]
		elif find[i]==(len(array)-1):
			array=array[ :(find[i])]
		else:
			half1=array[ :(find[i])]
			half2=array[(find[i])+1: ]
			array=half1+half2
	return array

