def smallerNumbersThanCurrent(nn):
    result = {}
    
    total=0
    for x in nn:
        if x in result:
            result[x]+=1
        else:
            result[x]=1
    mx=0
    for x, v in result.items():
        if v>mx:
            mx=x
    return mx
        

    

# Example usage
nums = [3,2,2,2,2,3]
output = smallerNumbersThanCurrent(nums)
print(output)  # Output: [4, 0, 1, 1, 3]
