import requests
import time
import random
import threading

# Specify the video URL and the number of views you want to simulate
url = "https://www.youtube.com/watch?v=pPjmA944Y88"
num_views = 100

# List of user agents to rotate through
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"
]

# Function to send a single request
def send_request():
    headers = {
        "User-Agent": random.choice(user_agents)
    }
    response = requests.get(url, headers=headers)
    print("View sent...")

# Function to send multiple requests
def send_requests(num_views):
    for i in range(num_views):
        send_request()
        time.sleep(random.uniform(0.5, 2))  # wait for a random time between 0.5 and 2 seconds

# Create multiple threads to send requests concurrently
threads = []
for i in range(10):  # create 10 threads
    thread = threading.Thread(target=send_requests, args=(num_views // 10,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All views sent.")
# def Tx(num, pv):
#     les=[]
#     eq=[]
#     gr=[]

#     length=len(num)

#     for x in range(length):
#         if pv> num[x]:
#             les.append(num[x])
#         elif pv==num[x]:
#             eq.append(num[x])
#         elif pv<num[x]:
#             gr.append(num[x])
    
#     return les+eq+gr






# nums = [9,12,5,10,14,3,10]
# pivot = 10
# print(Tx(nums, pivot))





# def Tx(nn):
#     box=[0]*len(nn)
  
            

# nums = [10,4,8,3]

# print(Tx(nums))


# class Solution:
#     def longestNiceSubstring(self, s):
#         def is_nice(sub):
#             chr = set(sub)
#             return all(c.lower() in chr and c.upper() in chr for c in chr)

#         long = ""
#         n = len(s)

#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 substring = s[i:j]
#                 if is_nice(substring) and len(substring) > len(long):
#                     long = substring

#         return long


# rs = Solution()
# print(rs.longestNiceSubstring("YazaAay"))  













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
        