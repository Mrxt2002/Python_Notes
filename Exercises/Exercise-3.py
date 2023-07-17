# display weight by interconverting
# between kg and pounds

weight= float(input("Weight : "))
param= str(input("(K)g or (L)bs :"))

if param =='k' or param=='K' :
    weight_inlbs= weight*((10**6)/454)
    print("Weight in kg : "+ str(weight))
    print("Weight in lbs : " + str(weight_inlbs))
elif param=='l' or param=='L' :
    weight_inKg= 0.454*weight
    print("Weight in lbs : " + str(weight))
    print("Weight in Kg : "+ str(weight_inKg))
else :
    print("Sorry ! wrong choice entered")