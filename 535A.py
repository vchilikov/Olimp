one = ["zero",
       "one",
       "two",
       "three",
       "four",
       "five",
       "six",
       "seven",
       "eight",
       "nine",
       "ten",
       "eleven",
       "twelve",
       "thirteen",
       "fourteen",
       "fifteen",
       "sixteen",
       "seventeen",
       "eighteen",
       "nineteen"]

ten = ["", "",
       "twenty",
       "thirty",
       "forty",
       "fifty",
       "sixty",
       "seventy",
       "eighty",
       "ninety"]

n = int(input())
if n < 20:
    print(one[n])
elif n % 10 == 0:
    print(ten[n // 10])
else:
    print(ten[n // 10] + "-" + one[n % 10])
