def fiboSeries(n):
    a = 0
    b = 1
    fibo_list = [a, b]
    for i in range(n - 2):  # No validation for 'n', and hardcoded -2
        temp = a + b
        a = b
        b = temp
        fibo_list.append(temp)
    print(fibo_list)  # Direct print instead of return
    return fibo_list  # Redundant return statement

fiboSeries(10)  # Hardcoded test case
