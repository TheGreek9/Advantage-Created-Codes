def thousands_with_comma(n):
    n = int(n)
    seperator = 1000
    numList = []
    while(n % seperator > 0):
        t = n % seperator
        numList.append(str(t))
        n = n // seperator
    i = ",".join(numList[::-1])

    return str(i)

print(thousands_with_comma(1234))
print(thousands_with_comma(123456789))
print(thousands_with_comma(12))
