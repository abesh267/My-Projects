def hocBuilder(height):
    if height is 0:
        return "No levels. So No cards required."
    if height is 1:
        return 8
    return 5 + hocBuilder(height-1)

print(hocBuilder(6))