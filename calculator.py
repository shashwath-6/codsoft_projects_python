import math
from pickle import FALSE

print("""1. ADDITION AND SUBTRACTION  \n2. MULTIPLICATION \n3.DIVISION \n4.PERCENTAGE FINDING \n5.TO FIND POWER \n6.SQUARE ROOT  \n7.QUIT OR CLOSE""")
true_or_false = True
"""VAL - BOOLEAN IT WILL EXECTUED THE LOOP IF TRUE AND IF USER ENTERS EXIT IT BECOMES FALSE CREATED BY SHASHWATH M"""
while true_or_false==True:
    choice = int(input("Enter your choice: "))
    """IT GET THE CHOICE FORM THE USER TO INDICATE WHICH ACTION SHOULD TAKE PLACE IN CODE CREATED BY SHASHWATH M"""
    if choice == 1:
        number = int(input("Enter the number of terms to be added : "))
        """IT'S NUMBER OF TERMS TO BE ADDED OR SUBTRACTED , WHICH HELPS TO EXECUTE THE LOOP TO nTIMES CREATED BY SHASHWATH M"""
        add_val = []
        """ITS A LIST WHICH STORE THE VALUES TO BE ADDED OR SUBTRACTED CREATED BY SHASHWATH M"""
        for i in range(number):
            x = int(input("Enter the number to be added : "))
            """IT GETS THE VALUE TO BE ADDED OR SUBTRACTED AND STORES IN THE LIST add_val CREATED BY SHASHWATH M"""
            add_val.append(x)
        print(sum(add_val))
    elif choice == 2:
        number = int(input("Enter the number of terms to be multiply : "))
        """IT'S NUMBER OF TERMS TO BE MULTIPLIED , WHICH HELPS TO EXECUTE THE LOOP TO nTIMES CREATED BY SHASHWATH M"""
        mul_val = []
        result =0
        """IT STORES THE VALUE OF MULTIPLIED TERMS IN THE LIST"""
        for i in range(number):
            x = int(input("Enter the number to be muliplied : "))
            """IT GETS THE VALUE TO BE MULTIPLIED AND STORES IN THE LIST mul_val CREATED BY SHASHWATH M"""
            mul_val.append(x)
        for i in range(1,number):
            result = mul_val[i-1]*mul_val[i]
        print(result)
    elif choice == 3:
        val_1 = float(input("Enter the numerator number : "))
        """ITS A VALUE OF NUMERATOR TERMS TO BE DIVIDED CREATED BY  SHASHWATH M"""
        val_2 = float(input("Enter the denominator number : "))
        """ITS A VALUE OF DENOMINATOR TERM TO BE DIVIDED CREATED BY  SHASHWATH M"""
        if val_2>0:
            print(val_1/val_2)
        else:
            print("ERROR YOU CANNOT DIVIDE A NUMER BY ZER0 \n THE ANSWER IS INFINITY")
    elif choice == 6:
        val=int(input("Enter the number to find the square root of : "))
        """ITS THE VALUE WHICH IS USED TO FIND THE SQUARE ROOT CREATED BY SHASHWATH M"""
        print(math.sqrt(val))
    elif choice == 4:
        part = int(input("Enter the number of part : "))
        """ITS THE VALUE OF WHICH REPRESENT THE TOP PART TO FIND THE PERCENTAGE CREATED BY SHASHWATH M"""
        whole = int(input("Enter the whole part : "))
        """ITS THE VALUE OF THE WHOLE TERMS OUT OF WHICH THE PERCENTAGE IS DETERMINED CREATED BY SHASHWATH M"""
        val = part/whole
        """IT'S A VARIABLE WHICH STORED THE RESULT OF PART NUMBER BY WHOLE PART GET_VALUE->INT AND RETURN_VAL->FLOAT CREATED BY SHASHWATH M"""
        print(val*100,"%")
    elif choice == 5:
        val = int(input("Enter the number to be  squared : "))
        """IT'S THE NUMBER TO FIND THE POWER OF TERMS CREATED BY SHASHWATH M"""
        power = int(input("Enter the power : "))
        """IT WILL GET THE VALUE OF POWER CREATED BY SHASHWATH M"""
        print(math.pow(val,power))
    elif choice == 7:
        true_or_false = FALSE
    else:
        print("Enter a valid choice ")
print("Thank You")
