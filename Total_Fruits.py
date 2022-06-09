class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitTypes, maxFruits, freq = 0, float('-Inf'), {}
        for end in range(0, len(fruits)):
            right = fruits[end]
            if right in freq.keys():
                freq[right] += 1
            else:
                freq[right] = 1
        # We need to shrink the window until we reach a frequency that is equal to 2
            while len(freq.keys()) > 2:
                left = fruits[fruitTypes]
                freq[left] -= 1

                if freq[left] == 0:
                    del freq[left]  # Delete
                fruitTypes += 1
            maxFruits = max(maxFruits, end-fruitTypes+1)
        return maxFruits
