def mid( str ):
    length = len(str)
    half = int(length/2)
    if (length % 2 == 0):
        return ""
    else: 
        return str[half:half+1]

print(mid("Testt"))