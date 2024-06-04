def subset(i,res,a):
    if i==len(a):
        print(res)
        return
    res.append(a[i])
    subset(i+1,res,a)
    res.pop()
    subset(i+1,res,a)

a=[1,2,3,4,5]
res=[]
print(subset(0,res,a))
