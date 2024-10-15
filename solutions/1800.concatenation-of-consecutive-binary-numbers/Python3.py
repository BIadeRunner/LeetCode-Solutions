class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        shift = 0

        for i in range(1, n + 1):
            # When i is a power of 2, increase the shift (binary length of new numbers)
            if i & (i - 1) == 0:
                shift += 1
            result = ((result << shift) + i) % MOD
        
        return result