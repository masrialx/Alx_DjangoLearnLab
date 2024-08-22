def Tx(nn):
    box=[0]*len(nn)
  
            

nums = [10,4,8,3]

print(Tx(nums))












# def Tx(nn):
#     box=[0]*len(nn)
#     lf=[0]*len(nn)
#     rh=[0]*len(nn)
#     for x in range(1,len(nn)):
#         lf[x]=lf[x-1]+nn[x-1]
   
    

        
#     for y in range(len(nn)-2,-1,-1):
#         rh[y]=nn[y+1]+rh[y+1]

#     for z in range(len(nn)):
#         box[z]=abs(lf[z]-rh[z])

#     return box
 
            

# nums = [10,4,8,3]

# print(Tx(nums))








# def Tx(nn):
#     box={}
#     total=0
#     for x in nn:
#         if x in box:
#             box[x]+=1
#         else:
#             box[x]=1
#     mx=0
#     for x, v in box.items():
#         if x+1 in box:
#             tt=box[x]+box[x+1]
#             if mx<tt:
#                 mx=tt
                
#     return mx
            

# nums = [1,1,1,1]
# print(Tx(nums))


















# class Solution:
#     def numOfPairs(self, nums, target):
#         freq = {}
#         for num in nums:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1
        
#         total = 0
        
#         for num in nums:
#             if target.startswith(num):
#                 complement = target[len(num):]
#                 if complement in freq:
#                     if complement == num:
#                         total += freq[complement] - 1
#                     else:
#                         total += freq[complement]
        
#         return total // 2


# s = Solution()
# print(s.numOfPairs(["777", "7", "77", "77"], "7777"))  
# print(s.numOfPairs(["123", "4", "12", "34"], "1234")) 
# print(s.numOfPairs(["1", "1", "1"], "11"))             




# class NumArray:
#     def Sum(self, nums, left=None, right=None):
#         if left is None and right is None:
#             # Initialize prefixSum if no indices are provided
#             self.prefixSum = [0] * (len(nums) + 1)
#             for i in range(len(nums)):
#                 self.prefixSum[i + 1] = self.prefixSum[i] + nums[i]
#         elif left is not None and right is not None:
#             # Compute the range sum using the prefixSum
#             return self.prefixSum[right + 1] - self.prefixSum[left]
#         else:
#             raise ValueError("Invalid arguments: Either provide no indices or both indices.")

# # Example usage:
# nums = [-2, 0, 3, -5, 2, -1]
# numArray = NumArray()
# numArray.Sum(nums)  # Initialize prefix sums
# print(numArray.Sum(left=2, right=5))  # Output: -1
# print(numArray.Sum(left=0, right=5))  # Output: -3










# class Solution:
#     def leftRightDifference(self, nums):
#         n = len(nums)
#         leftSum = [0] * n
#         rightSum = [0] * n
#         answer = [0] * n
        
      
#         for i in range(1, n):
#             leftSum[i] = leftSum[i - 1] + nums[i - 1]
        
       
#         for i in range(n - 2, -1, -1):
#             rightSum[i] = rightSum[i + 1] + nums[i + 1]
        
     
#         for i in range(n):
#             answer[i] = abs(leftSum[i] - rightSum[i])
        
#         return answer


# rs=  Solution()
# print(rs.leftRightDifference([10, 4, 8, 3]))  



# class Solution:
#     def findLHS(self, nums):
#         fq = {}
#         for num in nums:
#             if num in fq:
#                 fq[num] += 1
#             else:
#                 fq[num] = 1
        
 
#         mx = 0
#         for num in fq:
#             if num + 1 in fq:
#                 mx = max(mx, fq[num] + fq[num + 1])
        
#         return mx


# nums1 = [1,3,2,2,5,2,3,7]


# solution = Solution()
# print(solution.findLHS(nums1)) 








# class Solution:
#     def majorityElement(self, nums):
#         box = {}
       
#         for x in nums:
#             if x in box:
#                 box[x] += 1
#             else:
#                 box[x] = 1

#         max_count = 0
#         majority_element = None
#         for key, value in box.items():
#             if value > max_count:
#                 max_count = value
#                 majority_element = key
        
#         return majority_element


# nums = [2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2]
# rs = Solution()
# print(rs.majorityElement(nums))





# class Solution():
#     def isValid(self, s):
#         bx={')':'(',']':'[','}':'{'}
#         box=[]
#         for x in s:
#             if x in bx:
#                 bk = box and box.pop()
#                 if bx[x]!=bk:
#                     return False

#             else:
#                 box.append(x)
      
#         return not box



# rs= Solution()
# s="()()"
# print(rs.isValid(s))
        