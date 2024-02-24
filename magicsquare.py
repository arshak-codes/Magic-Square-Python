import numpy as np
def magic_square(n):
    square = np.zeros((n,n))
    p=n//2
    q=n-1
    square[p][q]=1
    for num in range(2,n**2+1):
        p=p-1
        q=q+1
        
        if q==n:
            q=0
        elif p==-1 and q==n:
            p=0
            q=(n-2)
        elif p==-1:
            p=(n-1)
        if square[p][q]!=0:
            p=p+1
            q=q-2
        square[p][q]=num
    print(square)
    
n = int(input("Enter Size Of Square: "))
magic_square(n)
                
        