import math


def getNumerator(fraction):
    """
    Method to get numerator from fraction

    :param fraction: for example 2/3
    :return numerator of fraction
    """

    numerator, trash = fraction.split('/')
    return int(numerator)


def getDenominator(fraction):
    """
    Method to get denominator from fraction

    :param fraction: for example 2/3
    :return denominator of fraction
    """

    trash, denominator = fraction.split('/')
    return int(denominator)


def getGSD(fraction1, fraction2):
    """
    Method to get GSD/NWD from 2 numbers

    :param fraction1: for example 2/3
    :param fraction2: for example 2/5
    :return: GSD of these numbers
    """

    denominator1 = getDenominator(fraction1)
    denominator2 = getDenominator(fraction2)

    while denominator1 != 0:
        c = denominator1
        denominator1 = denominator2 % denominator1
        denominator2 = c

    return denominator2


def sumFrictions(friction1, friction2):
    """
    Method to sum frictions

    :param friction1: for example 2/3
    :param friction2: for example 2/5
    :return: sum of frictions
    """

    numerator1 = getNumerator(friction1)
    numerator2 = getNumerator(friction2)

    denominator1 = getDenominator(friction1)
    denominator2 = getDenominator(friction2)

    GDS = getGSD(friction1, friction2)

    sumDenominator = denominator1 * denominator2 / GDS
    sumNumerator = sumDenominator * numerator1 / denominator1 + \
                   sumDenominator * numerator2 / denominator2

    # Reduce fractions (wyciaganie calosci)
    sumDenominator /= GDS
    sumNumerator /= GDS

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