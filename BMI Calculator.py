def bmi(h=int(input("Enter height(in cm): ")),w=int(input("Enter weight(in kg): "))):
    hm = h/100
    b = float(w/((hm*hm)))
    bf = "%.1f"%b
    if b < 18.5:
        print("Score is "+bf+". You are Underweight")
    elif b >= 18.5 and b < 25:
        print("Score is "+bf+". You are Normal")
    elif b >= 25 and b <= 30:
        print("Score is "+bf+". You are Overweight")
    else:
        print("Score is "+bf+". You are Obese")
        
        
        
bmi()