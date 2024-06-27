def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    minval = num1
    median = num1
    maxval = num1
    if minval < num2 and minval < num3:
        minval = minval
    elif num2 < num3 and num2 < minval:
        minval = minval
        median = num2
    else:
        minval = num3
        maxval = num1
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
