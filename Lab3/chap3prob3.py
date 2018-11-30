def get_Length(str):
    if theString == "": return 0
    return 1 + get_Length(str[1:])  
print(get_Length("hello"))
    

        
