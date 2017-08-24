import re

nums = {'0': [" _ ",
              "| |",
              "|_|",
              "   "], 
      '1': ["   ",
            "  |",
            "  |",
            "   "],
      '2': [" _ ",
            " _|",
            "|_ ",
            "   ",],
      '3': [" _ ",
            " _|",
            " _|",
            "   ",],
      '4': ["   ",
            "|_|",
            "  |",
            "   ",],
      '5': [" _ ",
            "|_ ",
            " _|",
            "   ",],
      '6': [" _ ",
            "|_ ",
            "|_|",
            "   ",],
      '7': [" _ ",
            "  |",
            "  |",
            "   "],
      '8': [" _ ",
            "|_|",
            "|_|",
            "   ",],
      '9': [" _ ",
            "|_|",
            " _|",
            "   ",],
}


def number(arr):
    if len(arr) != 4:
        raise ValueError
    for i in range(4):
        if len(arr[i]) % 3 != 0:
            raise ValueError
    result = ""
    piece = ["" for x in range(4)]
    num_numbers = int(len(arr[0]) / 3)
    for j in range(num_numbers):
        for i in range(4):
            piece[i] = arr[i][j * 3:(j + 1) * 3]
        found = False
        for n, k in zip(nums.keys(), nums.values()):
            if piece == k:
                result += n
                found = True
        if not found:
            result += "?"
    return result


def grid(num):
    if re.search("\D", num):
        raise ValueError
    result = ["" for x in range(4)]
    for ch in num:
        for i in range(4):
            result[i] += nums[ch][i]
    return result
