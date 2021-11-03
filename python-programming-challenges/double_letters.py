def double_letters(str):
    l = len(str)
    for i, c in enumerate(str):
        if (i+1 < l):
            print(i, c)
            print(i+1, str[i+1])
            if(c == str[i+1]):
                return True
        print("\n")
    else: return False
        
print(double_letters("Hello"))