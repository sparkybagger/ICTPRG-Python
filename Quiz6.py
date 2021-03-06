# Chelton Evans - Methods and functions quiz: 
# >>> s1 = "hello-there" 
# >>> s1.split("-") 
# ['hello', 'there'] 
# - this may help
#
# Write the function between the START and END tags
# START

def SortWordsAlphabetically(x): 
    words = x.lower().split("-")
    words.sort()
    return '-'.join(words)



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))