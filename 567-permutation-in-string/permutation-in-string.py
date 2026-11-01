class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Count characters in s1
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        # Build the first window
        for c in s2[:len(s1)]:
            window_count[c] = window_count.get(c, 0) + 1

        if s1_count == window_count:
            return True

        l = 0

        # Slide the window
        for r in range(len(s1), len(s2)):

            # Add the new character
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

            # Remove the leftmost character
            left_char = s2[l]
            window_count[left_char] -= 1

            if window_count[left_char] == 0:
                del window_count[left_char]

            l += 1

            # Compare frequencies
            if s1_count == window_count:
                return True

        return False