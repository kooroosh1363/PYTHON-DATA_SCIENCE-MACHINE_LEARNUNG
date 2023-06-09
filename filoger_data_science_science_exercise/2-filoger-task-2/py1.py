import numpy as np

# Receive input from the user
Num = int(input("Input :"))

# Create an array with random numbers
_Arr = np.random.randint(0, 101, size=Num)

# Display the array
print("Array : ", _Arr)


# Find the largest array value
Number_Max = np.max(_Arr)

# Display the largest value
print("Max: ", Number_Max)

# Check condition and display WIN or FAIL message
if Number_Max > 70:
    print("Output : WIN")
else:
    print("Output : FAIL")




