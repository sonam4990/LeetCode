class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # lengths must match
        if len(s) != len(goal):
            return False

        # goal must exist in doubled string
        return goal in (s + s) 