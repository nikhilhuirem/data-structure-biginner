# we are writing a code about factorial using recursion

def findFactorial(num: int)-> int:
    # first remember that if you are using recusion then there will be always think about the base case otherwise it will run in a infinite loop
    if num == 1:
        return 1
    else:
        return num * findFactorial(num-1)
    
ans = findFactorial(5)
print(ans)