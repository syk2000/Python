ls = [10,23,4,5,1,7]
is_even = True
for i in ls:
	if(is_even):
		print("짝수번째", i)
	else:
		print("홀수번째", i)
	is_even = not(is_even)