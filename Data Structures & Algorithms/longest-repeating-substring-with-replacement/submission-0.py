class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        longest = 0

        for right in range(len(s)):
            current_char = s[right]

            count[current_char] = count.get(current_char, 0) + 1

            max_frequency = max(
                max_frequency,
                count[current_char]
            )

            while (right - left + 1) - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest