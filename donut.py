prc = int(input("enter the price of donut: Rs."))
qty=int(input("enter the no. of donut:"))
amt=prc*qty

if amt>1000:
    print("discount of 10% is applicable")
    dis=amt*10/100
    amt=amt-dis
else:
    print("discount of 5%is applicable")
    dis=amt*5/100
    amt=amt-dis

print("total amount is : Rs.",amt)

            
              
              
            
