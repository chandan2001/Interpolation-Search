def interpolationSearch(arr, n, x, eggs):
    #indices of lowest and highest floors
    lo=0
    hi=n-1
    step=0

    # Since array is sorted
    # an element present in array must be
    # in range defined by corner 

    if ar[lo]==0: # if all floors are UNSAFE for the egg
        step+=1
        print("all floors are NOT SAFE for the eggs")
        eggs-=1
        print("eggs remained = " + str(eggs))
        print("number of steps = " + str(step))
        return lo

    elif ar[hi]==1: # if all floors are SAFE for the egg
        step+=1
        print("all floors are SAFE for the eggs")
        print("eggs remained = " + str(eggs))
        print("number of steps = " + str(step))
        return hi

    # applying INTERPOLATION SORT

    while lo<=hi and x>=arr[lo] and x<=arr[hi]: 
        if lo==hi: # for only one floor
            steps+=1
            if ar[lo]==0:
                print("floor is NOT safe")
                eggs-=1
            elif ar[lo]==1:
                print("floor is safe")
            print("eggs remained = " + str(eggs))
            print("number of steps = " + str(step))
            return lo

        if ar[lo]==1 and ar[lo+1]==0: # Condition of target found
            step+=1
            eggs-=1
            print("eggs remained = " + str(eggs))
            print("number of steps = " + str(step))
            return lo
          
        # Probing the position with keeping uniform distribution in mind. 

        pos = lo + int((float(hi - lo) / ( arr[hi] - arr[lo])) * ( x - arr[lo])) 

        if ar[pos]==0 and ar[pos-1]==1: # Condition of target found
            step+=1
            print("eggs remained = " + str(eggs))
            print("number of steps = " + str(step))
            return pos 

        if ar[pos]==1 and ar[pos+1]==0: # Condition of target found
            step+=1
            eggs-=1
            print("eggs remained = " + str(eggs))
            print("number of steps = " + str(step))
            return pos 
   
        # If x is larger, x is in upper part 
        elif ar[pos]==1 and ar[pos+1]==1:
            step+=1
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        elif ar[pos]==0 and ar[pos-1]==0: 
            step+=1
            eggs-=1
            hi = pos - 1; 

    print("eggs remained = " + str(eggs))
    print("number of steps = " + str(step))
    return -1


# floors assigned
lowest=2
print("lowest floor assigned = " + str(lowest))
highest=4
print("highest floor assigned = " + str(highest))
print("")

egg=4
print("initial number of eggs = " + str(egg))

# creating array on which all processing will be done
# this will not be there in the output
arr=[]
for i in range(highest-lowest+1):
    arr.append(i+lowest)

n=highest-lowest+1
print("number of floors provided = " + str(n))
print("")

x = 3 # Element to be searched
print("search critical floor " + str(x))
print("")

# main array which describes safety of egg
# this will not be there in the output
# '1' means safe and '0' means unsafe
ar=[]
for i in range(min(x-1,highest-lowest+1)):
    ar.append(1)
for i in range(min(x-1,highest-lowest+1),highest-lowest+1):
    ar.append(0)
print(arr)
print(ar)
print("")

index = interpolationSearch(arr, n, x, egg)
  
print("Critical floor found : " + str(arr[index]))
print("")
