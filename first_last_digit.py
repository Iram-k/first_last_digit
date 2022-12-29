def firstDigit(n) :  # Find the first digit 

	# Remove last digit from number 
	# till only one digit is left 
	while n >= 10: 
		n = n / 10; 
	
	# return the first digit 
	return int(n) 

def lastDigit(n) : # Find the last digit 

	# return the last digit 
	return (n % 10) 

n = int(input("Enter a Number : ")) 
print(firstDigit(n), end = " ") 
print(lastDigit(n)) 
