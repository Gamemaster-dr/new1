
def list_num(param_list):
    for param in param_list:
        if param % 2 == 0:
            print(f"偶数:{param}")
        else:
            print(f"奇数:{param}")
            

if __name__ == "__main__":
    print(__name__)
    param_list = [1,2,3,4,5,10,20,30]
    list_num(param_list)

