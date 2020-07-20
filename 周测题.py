def sequence(n):
    if n%2==1:
        half=(n+1)//2
    else:
        half=n//2
    for i in range(1,half):
        list=[]
        sum=0
        for j in range(i,half+1):
            list.append(j)
            sum+=j
            if sum==n:
                print(list)
            elif sum>n:
                break
sequence(20)

