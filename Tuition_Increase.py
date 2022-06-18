def toFixed(value, digits):
    return "%.*f" % (digits, value)

print("What is the amount of the starting tuition [Decimals may be entered, 5000.75, 8000.00 etc]?")

# user inputs variable amounts
tuition = float(input())
print("What is the percentage of increase [enter in decimal format such as (for 3$, Type 0.09), (5%, Type 0.05) etc.]?")
percentIncrease = float(input())
print("How many years are you projecting the tuition increase? [Enter whole numbers only]")
years = int(input())
print("===================================================================")
print("PROJECTED TUITIONS (PER SEMESTER FOR FULL-TIME STUDENTS)")
print("===================================================================")
print("YEAR         PROJECTED TUITION")
print("===================================================================")

# FOR LOOP to calculate percentage increase
for count in range(1, years + 1, 1):
    
    # formula to calculate percentage increase
    tuition = tuition * (1 + percentIncrease)
    
    # output statement to show projected tuition amount and round the decimals 2 points to the right
    print("Year " + format(count) + " :            $" + toFixed(tuition,2))

# final output statements
print("===================================================================")
print("THESE PROJECTIONS REFLECT A " + format(percentIncrease * 100) + " % ANNUAL INCREASE")
print("===================================================================")

# END PROGRAM
