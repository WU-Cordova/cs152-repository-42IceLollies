

def main():
    
    curr_num = 7
    doubled = 2* curr_num

    def is_prime(num, div = 2):
        if div == int(num ** 0.5)+1:
            return True
        
        if num % div == 0:
            return False
        
        return is_prime(num, div +1)
    

    while not is_prime(doubled):
        doubled+=1

    
    print(doubled)



if __name__ == '__main__':
    main()
