




class Solution:
    
    def threeSum(self,nums):
        nums.sort()

        result =[]
        middle_result= []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for n in range(j+1,len(nums)):
                    
                    if nums[i]+nums[j]+nums[n] == 0:
                        middle_result.append(nums[i])
                        middle_result.append(nums[j])
                        middle_result.append(nums[n])
                        
                        if middle_result not in result :
                            result.append(middle_result)
                        middle_result = []
        
        return result
    
    
    

if __name__ == '__main__':
    
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
