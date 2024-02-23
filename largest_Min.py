"""Finding_Largest_And_Minimum_Numbers"""

max = 0
min = 0

numbers = int(input('Enter numbers: '))
for number in range(1, 5):
		
	
	if numbers > number:
		max = numbers
	if numbers < number:
		min = number
	numbers = int(input('Enter numbers: '))

print(max)
print(min)