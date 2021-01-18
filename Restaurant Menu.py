def chillox(b,p="mohakhali"):
    b=b.lower()
    p=p.lower()
    if p == "mohakhali":
        if b == "bbq chicken cheese burger":
            payment = 250+40+(250*0.08)
            print(payment)
        elif b == "beef burger":
            payment = 170+40+(170*0.08)
            print(payment)
        elif b == "naga drums":
            payment = 200+40+(200*0.08)
            print(payment)
    else:
        if b == "bbq chicken cheese burger":
            payment = 250+60+(250*0.08)
            print(payment)
        elif b == "beef burger":
            payment = 170+60+(170*0.08)
            print(payment)
        elif b == "naga drums":
            payment = 200+60+(200*0.08)
            print(payment)
chillox("Beef Burger", "dhanmondi")
chillox("Beef Burger")