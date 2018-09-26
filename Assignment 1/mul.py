import time, sys
from random import randint

# To run this program
# python -m memory_profiler mul.py

# Functions
@profile
def random_n_digit(digits):	# Generation of random numbers
	neg = randint(0,1)
	if neg==0:
		neg = -1
	else:
		neg = 1
	number_1 = 10**(digits-1)
	number_2 = (10**digits)-1
	return neg*randint(number_1,number_2)

@profile
def random_generate(number_of_digits):
	for i in range(0, 1000):
		number_1 = int(random_n_digit(number_of_digits))
		number_2 = int(random_n_digit(number_of_digits))
		number_1_array.append(number_1)
		number_2_array.append(number_2)

@profile
def multiply(n, m):  # Recursive multiplication of two numbers
	if m == 0:
		return 0
	elif m < 0:
		return -(n - multiply(n, m+1))
	else:
		return n + multiply(n, m-1)

@profile
def bitWise(a, b): 
	result = 0 

	while (b > 0): 
		if (b & 1): #checks if b is odd
			result = result + a 
		a = a << 1
		b = b >> 1

	return result

@profile
def bit():
	for i in range(0, 1000):
		# m = multiply(number_1_array[i], number_2_array[i])
		# numb = number1
		# for j in range(0, abs(number_2_array[i])-1):
		# 	number1 = number1 + temp
		# multiplication = int(number_1_array[i] * number_2_array[i])
		multiplication = bitWise(number_1_array[i], number_2_array[i])
		# print(multiplication)

@profile
def my_main():
	globals()['number_1_array'] = []
	globals()['number_2_array'] = []
	#number_of_digits = int(input("number_of_digits = "))
	random_generate(512)
	start = time.time()
	bit()
	# xxxx-----xxxxx
	end = time.time()
	print(end - start)


# xxxx-----xxxxx
if __name__ == '__main__':
	# sys.setrecursionlimit(9999)
	my_main()