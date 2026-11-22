num_str = "42"
num_int = int(num_str) # convert string to integer
print(num_int + 1)

# Error: 
# print(num_str + 1)

float_str = "3.14"
float_num = float(float_str) # convert string to float
print(float_num + 2.19)

# Error:
# print(num_str + 2.19)

int_num = 7
float_num = float(int_num) 
print(float_num)

float_num2 = 9.99
int_num2 = int(float_num2) # convert float to integer
print(int_num2)

num = 20
num_str2 = str(num) # convert integer to string
print("this shirt costs $" + num_str2)
      
# Error:
# print("this shirt costs $" + num)