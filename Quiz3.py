# Write the function between the START and END tags
# START

def FibonacciAdder(x):
    if x < 2:
        return 0
    a = 0
    b = adder = 1
    for n in range(x-2):
        a, b = b, a + b 
        adder += b
    return adder 

    
# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))