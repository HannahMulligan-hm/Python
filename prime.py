# def is_prime(n):
# 	for i in range(2,n-1):
# 		if i < 2:
# 			continue
# 		elif n % i == 0:
# 			return False 
# 		else:
# 			return True

# print(is_prime(23))

# def is_prime(n):
# 	for i in range(2, n-1):
# 		if n % i == 0:
# 			print(n,i)
# 			return False
# 		else:
# 			print(n,i)
# 			return True

# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(975))
# print(is_prime(2))
# print(is_prime(197))

def is_prime(n):
	if n > 2:
		for i in range(2, n-1):
			if (n % i)== 0:
				return False
		return True
			# if (n % i) != 0:
			# 	print(n,i)
			# 	return True
	else:
		return True

print(is_prime(7))
print(is_prime(8))
print(is_prime(975))
print(is_prime(2))
print(is_prime(197))
