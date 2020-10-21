from time import time
import matplotlib.pylab as plt
#the string way
def digit_adder(number):
    if number < 10 :
        return number
    else:
        string_number=str(number)
        sum_up=0
        for item in string_number:
            sum_up += int(item)
        return digit_adder(sum_up) 
#the math way
def sumdigits(n):
    if n < 10:
        return n
    else:
        Sum = 0
        digit_count = 0 # the variable to keep track the number of digits in the number
        while n > 0:
            digit_count += 1
            Sum += n % 10
            n //= 10
        n = Sum # main number update
        if digit_count > 1:
            return sumdigits(n) # recursion happens based on the condition

#function to count 0 and 1 from start to stop by string way
def zero_one_digit_counter_str(start, stop):
    list1=[]
    list2=[]
    for number in range(start , stop):
        if digit_adder(number)==1:
            list1.append(number)
        elif digit_adder(number)==2:
            list2.append(number)
    return len(list1) , len(list2)
#function to count 0 and 1 from start to stop by math way
def zero_one_digit_counter_math(start, stop):
    list1=[]
    list2=[]
    for number in range(start , stop):
        if sumdigits(number)==1:
            list1.append(number)
        elif sumdigits(number)==2:
            list2.append(number)
    return len(list1) , len(list2)
#in this func. we are using the time() to calculate the elapsed time of each funcion and try to show the result in a line chart
def av_time(start=0):
    #the list of periods which will be given to two funcitons (you can change the periods if you want)
    period_list=[100,1000,10000,100000,500000,]
    #result dictionary for saving the result of each method
    result_str={}
    result_math={}
    for item in period_list:   
    #the string way
        t1=time()
        zero_one_digit_counter_str(start, item)
        st=time()-t1
        result_str.update({item:st})

        #the math way
        t1=time()
        zero_one_digit_counter_math(start, item)
        mt=time()-t1
        result_math.update({item:mt})
#using mathplotlib to show the result of the performance of each functions saved in the dictionaries

    lists_str = sorted(result_str.items()) # sorted by key, return a list of tuples
    lists_math = sorted(result_math.items()) # sorted by key, return a list of tuples
    x,y=zip(*lists_str) # unpack a list of pairs into two tuples (the bue line)
    v,u=zip(*lists_math) # unpack a list of pairs into two tuples ( the orange line)
    plt.plot(x,y,v,u)
    plt.ylabel("the time execution(s)")
    plt.xlabel("the periods (number)")
    plt.title("digit adder mehods line chart ")
    plt.show()
    return f'the str way: {result_str} \n  and the math way : {result_math}'
            

    
tm = av_time()
print(tm)
#time alapsed of string 






