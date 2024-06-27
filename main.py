def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    minval = num1
    median = num1
    maxval = num1
   # Three different sections from or labs
    if num2 < minval:
        minval = num2
        if num3 < minval:
            minval = num3
    # ^this found the min
    if num2 > maxval:
        maxval = num2
        if num3 > maxval:
            maxval = num3
    # ^This found the max
    if num1 > minval and num1 < maxval:
        median = num1
    elif num2 > minval and num2 < maxval:
        median = num2
    else:
        median = num3
    # ^ this found the median
    print(f'{minval} {median} {maxval}')
        
    
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
