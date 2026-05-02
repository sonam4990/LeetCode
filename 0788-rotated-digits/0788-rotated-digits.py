class Solution:
    def rotatedDigits(self, n: int) -> int:

        # valid rotations
        valid = {'0', '1', '2', '5', '6', '8', '9'}

        # digits that change after rotation
        change = {'2', '5', '6', '9'}

        count = 0

        for num in range(1, n + 1):

            s = str(num)

            is_valid = True
            is_changed = False

            for ch in s:

                # invalid digit
                if ch not in valid:
                    is_valid = False
                    break

                # becomes different after rotation
                if ch in change:
                    is_changed = True

            # good number
            if is_valid and is_changed:
                count += 1

        return count