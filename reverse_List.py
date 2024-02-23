def reverse_List(numbers):
	while(numbers != 0):
		if numbers[0] > numbers[1]:
			temp = numbers[0]
			numbers[0] = numbers[1]
			numbers[1] = temp
			reurn numbers

sample_List = [10, 2, 8, 9, 3, 4, 1, 5]
print(reverse_List(sample_List))

