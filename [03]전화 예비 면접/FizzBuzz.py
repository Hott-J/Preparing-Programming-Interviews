for i in range(101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#가장 먼저 3과 5가 나눠떨어지는지부터 해야한다.