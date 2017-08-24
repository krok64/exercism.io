def numeral(num):
    result = []
    
    thousands = int(num / 1000)
    for i in range(thousands):
        result.append("M")
    
    hundreds = int((num - thousands * 1000) / 100)
    if hundreds==9:
        result.append("CM")
    elif hundreds==8:
        result.append("DCCC")
    elif hundreds==7:
        result.append("DCC")
    elif hundreds==6:
        result.append("DC")
    elif hundreds==5:
        result.append("D")
    elif hundreds==4:
        result.append("CD")
    elif hundreds==3:
        result.append("CCC")
    elif hundreds==2:
        result.append("CC")
    elif hundreds==1:
        result.append("C")
    
    tens = int((num - thousands * 1000 - hundreds * 100) / 10)
    if tens==9:
        result.append("XC")
    elif tens==8:
        result.append("LXXX")
    elif tens==7:
        result.append("LXX")
    elif tens==6:
        result.append("LX")
    elif tens==5:
        result.append("L")
    elif tens==4:
        result.append("XL")
    elif tens==3:
        result.append("XXX")
    elif tens==2:
        result.append("XX")
    elif tens==1:
        result.append("X")

    ones = int(num - thousands * 1000 - hundreds * 100 - tens * 10) 
    if ones==9:
        result.append("IX")
    elif ones==8:
        result.append("VIII")
    elif ones==7:
        result.append("VII")
    elif ones==6:
        result.append("VI")
    elif ones==5:
        result.append("V")
    elif ones==4:
        result.append("IV")
    elif ones==3:
        result.append("III")
    elif ones==2:
        result.append("II")
    elif ones==1:
        result.append("I")

    return "".join(result)
