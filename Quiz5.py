# Write the function between the START and END tags
# START

def IsPalindrome(x):
    x = str(x.lower)
    rev = reversed(x)

    if x != rev:
        status = True
    else: 
        status = False
    
    return status



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("Frank") == False))