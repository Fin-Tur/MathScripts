def convertToDecimal(num, base):
    res = 0
    for i in range(0, len(num)):
        if num[i] == "A":
            res += 10 * (pow(base, len(num) - i - 1))
        elif num[i] == "B":
            res += 11 * (pow(base, len(num) - i - 1))
        elif num[i] == "C":
            res += 12 * (pow(base, len(num) - i - 1))
        elif num[i] == "D":
            res += 13 * (pow(base, len(num) - i - 1))
        elif num[i] == "E":
            res += 14 * (pow(base, len(num) - i - 1))
        elif num[i] == "D":
            res += 15 * (pow(base, len(num) - i - 1))
        else:
            res += int(num[i]) * (pow(base, len(num) - i - 1))
    return res


def convertToBaseX(n, basis):
    if n == 0:
        return "0"
    zahlen = "0123456789ABCDEF"  # Unterstützt bis zur Basis 16
    ergebnis = ""
    while n > 0:
        ergebnis = zahlen[n % basis] + ergebnis
        n //= basis
    return ergebnis


def romantoInt(numR: str) -> int:
    numD = 0

    for i in range(len(numR)):
        if numR[i] == "I":
            if i + 1 < len(numR) and (numR[i + 1] == "V" or numR[i + 1] == "X"):
                numD -= 1
            else:
                numD += 1

        elif numR[i] == "V":
            numD += 5

        elif numR[i] == "X":
            if i + 1 < len(numR) and (numR[i + 1] == "L" or numR[i + 1] == "C"):
                numD -= 10
            else:
                numD += 10

        elif numR[i] == "L":
            numD += 50

        elif numR[i] == "C":
            if i + 1 < len(numR) and (numR[i + 1] == "D" or numR[i + 1] == "M"):
                numD -= 100
            else:
                numD += 100

        elif numR[i] == "D":
            numD += 500

        elif numR[i] == "M":
            numD += 1000

    return numD


def intTRoman(numD: int) -> str:
    numR = ""
    strD = str(numD)
    l = len(strD)
    print(strD[0])
    i = 0

    while numD > 0:

        if strD[i] == "4" or strD[i] == "9":

            if strD[i] == "4":
                if l - i == 1:
                    numR += "IV"
                    numD -= 4
                elif l - i == 2:
                    numR += "XL"
                    numD -= 40
                elif l - i == 3:
                    numR += "CD"
                    numD -= 400

            elif strD[i] == "9":
                if l - i == 1:
                    numR += "IX"
                    numD -= 9
                elif l - i == 2:
                    numR += "XC"
                    numD -= 90
                elif l - i == 3:
                    numR += "CM"
                    numD -= 900

        else:
            if numD >= 1000:
                numR += "M"
                numD -= 1000
            elif numD >= 500:
                numR += "D"
                numD -= 500
            elif numD >= 100:
                numR += "C"
                numD -= 100
            elif numD >= 50:
                numR += "L"
                numD -= 50
            elif numD >= 10:
                numR += "X"
                numD -= 10
            elif numD >= 5:
                numR += "V"
                numD -= 5
            elif numD >= 1:
                numR += "I"
                numD -= 1

        print("numR : " + numR + " - numD : " + str(numD))
        strD = str(numD)
        l = len(strD)

    return numR
