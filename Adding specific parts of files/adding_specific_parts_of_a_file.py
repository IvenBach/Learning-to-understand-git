# Code Above

def adding_two_numbers_together(augend, addend):
    return augend + addend

def subtracting_two_numbers(minuend, subtrahend):
    return minuend - subtrahend

def multiplying_two_numbers(multiplier, multiplicand):
    return multiplier * multiplicand

def dividing_two_numbers(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator

# Plenty of code in between


# Code you're working on
def Foo(bar, bazz):
    match bar:
        case 1:
            return adding_two_numbers_together(1, 3)
        case 2:
            return subtracting_two_numbers(2, 2)
        case 3:
            return multiplying_two_numbers(3, 1)
        case 4:
            return dividing_two_numbers(4, 0)

    return bazz
