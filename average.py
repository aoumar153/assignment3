def avg(a):
    s = 0
    l = len(a)
    #print(l)
    for i in range(len(a)):
        s = s+ a[i]
    average = s/l
    #print(average)
    return average

avg([2,3])