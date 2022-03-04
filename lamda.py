from functools import reduce
def run():
    
    my_list=[1,2,3,4,5]
    old=list(filter(lambda x: x%2 !=0, my_list))
    print(old)
    my_list2=[1,2,3,4,5]
    squares=list(map(lambda x:x**2,my_list2))
    print(squares)
    my_list3=[2,2,2,2,2]
    total=reduce(lambda a,b:a*b ,my_list3)
    print(total)
if __name__=="__main__":
    run()