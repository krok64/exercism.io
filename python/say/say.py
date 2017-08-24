def say(num_orig):

    word_100 = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 
      10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
      20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred'}
    word_razrad = ['', 'thousand', 'million', 'billion']

    if num_orig < 0 or num_orig >= 1e12:
        raise AttributeError
    if num_orig==0:
        return word_100[num_orig]

    razrad_max = len(split_by_num(str(int(num_orig)), 3)) - 1
    rez = []
    for idx, chunk in enumerate(split_by_num(str(int(num_orig)), 3)):
        num = int(chunk)
        a = int(num / 100)
        if a > 0:
            rez.append(word_100[a])
            rez.append(word_100[100])
            if a * 100 != num:
                rez.append("and")
        num = num - a * 100
        if num_orig>100 and num>0 and razrad_max-idx==0 and a==0:
            rez.append("and")
        if num>0 and num<21:
            rez.append(word_100[num])
        elif num>0 and num<100:
            tens = int(num / 10) * 10
            ones = num - tens
            if ones>0:
                rez.append(word_100[tens]+'-'+word_100[ones])
            else:
                rez.append(word_100[tens])
        if int(chunk)>0 and razrad_max-idx >= 1:
            rez.append(word_razrad[razrad_max-idx])
    return " ".join(rez)

def split_by_num(s, num):
    rez = []
    while s:
        rez.append(s[-num:])
        s = s[:-num]
    return rez[::-1]

if __name__ == '__main__':
    print(say(123456789))