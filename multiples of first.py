# list of multiples of first element with second element consective time


def list_of_multiples(num,length):
	return[i*num for i in range(1,length)]

print(list_of_multiples(5,5))

# solution 2

def list_of_multiples(num,length):
	list = []
	for i in range(length):
		list.append(num+i*num)
	return list

print(list_of_multiples(10,2))