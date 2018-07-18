input = raw_input("Enter 1 to convert from Celsius to Fahrenheit or 2 to convert from Fahrenheit to Celsius: ");
try:
	input = int(input);
	if(input == 1):
		input = raw_input("Enter temperature in Celsius: ");
		celsius = int(input);
		fahrenheit = (celsius * 9/5) + 32 ;
		print fahrenheit;
	elif(input == 2):
		input = raw_input("Enter temperature in Fahrenheit: ");
		fahrenheit = int(input);
		celsius = (fahrenheit - 32) * 5/9;
		print celsius;
except ValueError:
	print "Invalid input";

