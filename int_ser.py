def interpolationSearch(arr, n, x): 
    # Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
    step=1

    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos = lo + int((float(hi - lo) / ( arr[hi] - arr[lo])) * ( x - arr[lo])) 
        print("low = " + str(lo) + " and high = " + str(hi))
        print("pos = " + str(pos))
        # Condition of target found 
        if arr[pos] == x: 
            print("step = " + str(step))
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x:
            step+=1
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            step+=1
            hi = pos - 1; 

    print("step = " + str(step))
    return -1

# Driver Code 
# Array of items on which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print(arr)
n = len(arr)
print("size of array = " + str(n))
x = 18 # Element to be searched 
print("search " + str(x))

index = interpolationSearch(arr, n, x) 
  
if index != -1: 
    print("Element found at index : " + str(index)) 
else: 
    print("Element not found")
