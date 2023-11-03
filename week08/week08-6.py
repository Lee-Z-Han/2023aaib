class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        N = len(arr) # 小心, 題目不是 a 是 arr

        for k in range(N):
            for i in range(1,N):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]

        for i in range(1,N):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True