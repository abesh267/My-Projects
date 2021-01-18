def replace_domain(ea,nd,od="kaaj.com"):
    x=ea.split("@")
    x1=x[1]
    if x1 == "kaaj.com":
        x1="sheba.xyz" 
        a=x[0]+"@"+x1
        print("Changed:",a)
    else:
        print("Unchanged:",ea)
    
    
replace_domain("alice@kaaj.com","sheba.xyz","kaaj.com")
replace_domain("bob@sheba.xyz","sheba.xyz")