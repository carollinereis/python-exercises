import logging

logger = logging.getLogger(__name__)

def calculator():
	"""
	Simple calculator that performs basic operations (+, -, /, *) on two numbers.
	The program continues to prompt for input until the user chooses to exit.
	"""
	while True:							               								
		number_1 = input('Enter a number: ')         
		operator = input('Choose an operator (+-/*): ')
		number_2 = input('Enter another number: ')  
							
		valid_number = None  
		num_1_float = 0         
		num_2_float = 0
		
		try:							
			num_1_float = float(number_1)
			num_2_float = float(number_2)
			valid_number = True
		except:
			valid_number = None

		if valid_number is None:
			logger.warning('Oops, one or more numbers are invalid!')
			continue

		allowed_operators = '+-/*'		
												
		if operator not in allowed_operators:	
			logger.warning('Invalid operator!')
			continue

		if len(operator) > 1:				
			logger.warning('Enter only one operator!')
			continue

		if operator == '+':
			print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
		elif operator == '-':
			print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
		elif operator == '/':
			print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
		elif operator == '*':
			print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
		else:
			logger.warning('Hm, something is wrong. Try again!')
			continue

		exit = input('Enter [q] to quit: ').lower().startswith('q')
		if exit is True:
			print('Thanks for using the calculator!') 
			break
if __name__ == '__main__':
    calculator()