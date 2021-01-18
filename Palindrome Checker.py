def pal(x):
    y=x.replace(" ","")
    p=y[::-1]
    if p==y:
        print("Palindrome")
    else:
        print("Not a palindrome")
  

pal("madam")
pal("hello")
pal("nurses run")