gifts = {12: "twelve Drummers Drumming", 11: "eleven Pipers Piping", 10: "ten Lords-a-Leaping",
  9: "nine Ladies Dancing", 8: "eight Maids-a-Milking", 7: "seven Swans-a-Swimming",
  6: "six Geese-a-Laying", 5: "five Gold Rings", 4: "four Calling Birds", 3: "three French Hens",
  2: "two Turtle Doves", 1: "a Partridge in a Pear Tree.\n"}

days = {1: "first", 2: "second", 3:"third", 4:"fourth", 5:"fifth", 6:"sixth", 7:"seventh", 8:"eighth", 9:"ninth", 10:"tenth", 11:"eleventh", 12:"twelfth"}


def verse(num):
    result = "On the %s day of Christmas my true love gave to me, " % days[num]
    for i in range(num, 1, -1):
        result += gifts[i] + ", "
    if num != 1:
        result += "and "
    result += gifts[1]
    return result

def verses(n, m):
    result = ""
    for i in range(n, m + 1):
        result += verse(i)+"\n"
    return result

def sing():
    return verses(1, 12)