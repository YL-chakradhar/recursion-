def Binary(size,result,n):
    if size==n:
        print(result)
        return
    Binary(size+1,result+'1',n)
    Binary(size+1,result+'0',n)
n=4
print(Binary(0,"",4))