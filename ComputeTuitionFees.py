# Program to calculate the Tuition Fees for 10 years

year = 0
tuitionFees = 10000

while year < 10 :
    tuitionFees = tuitionFees + (tuitionFees * 0.05)
    year = year + 1
    print(tuitionFees)
    
print("Tuition Fees after 10 years " , tuitionFees)    
