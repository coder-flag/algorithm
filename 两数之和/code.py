class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 返回nums升序排列的下标
        sorted_id = sorted(range(len(nums)), key=lambda k:nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:
                tail -= 1
            elif sum_result < target:
                head  += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]