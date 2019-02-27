for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i+j+k==1000 and ( (i*i+j*j==k*k) or (i*i==j*j+k*k) or (i*i+k*k==j*j)) :
                print(i,j,k,i*j*k)
                break
