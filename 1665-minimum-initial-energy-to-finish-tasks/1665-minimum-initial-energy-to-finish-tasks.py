class Solution:
    def minimumEffort(self, tasks):
        
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            # If current energy is less than minimum
            if current < minimum:

                # Add extra energy needed
                extra = minimum - current
                energy += extra
                current += extra

            # Do the task
            current -= actual

        return energy