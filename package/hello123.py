def fact(num):
    '''Return the factorial of a given number'''
    sum1=1
    for i in range(num,1,-1):
        sum1*=i
    return sum1
