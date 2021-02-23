import math


def getNumerator(fraction):
    """
    Method to get numerator from fraction

    :param fraction: for example 2/3
    :return numerator of fraction
    """

    numerator = fraction.split('/')[0]
    return int(numerator)


def getDenominator(fraction):
    """
    Method to get denominator from fraction

    :param fraction: for example 2/3
    :return denominator of fraction
    """

    denominator = fraction.split('/')[1]
    return int(denominator)


def getGSD(number1, number2):
    """
    Method to get GSD/NWD from 2 numbers

    :param number1: for example 2/3
    :param number2: for example 2/5
    :return: GSD of these numbers
    """

    while number1 != 0:
        c = number1
        number1 = number2 % number1
        number2 = c

    return number2


def sumFrictions(fraction1, fraction2):
    """
    Method to sum frictions

    :param fraction1: for example 2/3
    :param fraction2: for example 2/5
    :return: sum of frictions
    """

    numerator1 = getNumerator(fraction1)
    numerator2 = getNumerator(fraction2)

    denominator1 = getDenominator(fraction1)
    denominator2 = getDenominator(fraction2)

    GDS = getGSD(getDenominator(fraction1), getDenominator(fraction2))

    sumDenominator = denominator1 * denominator2 / GDS
    sumNumerator = sumDenominator * numerator1 / denominator1 + \
                   sumDenominator * numerator2 / denominator2

    # Reduce fractions (skracanie ulamkow)
    reduceGSD = getGSD(sumNumerator, sumDenominator)
    sumDenominator /= reduceGSD
    sumNumerator /= reduceGSD

    return str(int(sumNumerator)) + "/" + str(int(sumDenominator))


def pullOutFraction(fraction):
    """
    Method to pull out fractions

    :param fraction: for example 4/3
    :return: pull outed fraction for example: 1 1/2
    """

    numerator = getNumerator(fraction)
    denominator = getDenominator(fraction)

    if numerator >= denominator:
        number = math.floor(numerator / denominator)
        fraction = str(numerator % denominator) + "/" + str(denominator)

        return f"{number} {fraction}"
    else:
        print(f"You're not able to pull out this fraction: {numerator}/{denominator}")
        return fraction


# Sum of 2 fractions
frictionA = input('Type first fraction; For example 2/3\n')
frictionB = input('Type second fraction; For example 4/7\n')

sumFrictionsAB = sumFrictions(frictionA, frictionB)

print(f"\nResult (wynik sumowania ulamkow):\n {sumFrictionsAB}")
print("\nPull out (wyciaganie calosci):\n", pullOutFraction(sumFrictionsAB))