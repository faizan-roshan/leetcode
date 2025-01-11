from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        # Initialize pointers:
        # 'i' to traverse through the list
        # 'wp' (write pointer) to overwrite the characters and counts
        i = 0
        wp = 0
        n = len(chars)

        # Traverse through the array
        while i < n:

            # Store the current character to process its group
            ch = chars[i]
            count = 0

            # Count the occurrences of the current character
            while i < n and chars[i] == ch:
                count += 1
                i += 1

            # Write the character to the write pointer position
            chars[wp] = ch
            wp += 1

            # If the count is greater than 1, write its digits to the array
            if count > 1:
                for digit in str(count):
                    chars[wp] = digit
                    wp += 1

        # Return the length of the compressed string
        return wp
