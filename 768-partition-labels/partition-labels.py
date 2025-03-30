class Solution:
    def partitionLabels(self, s: str):
        last_occurrence = {char: idx for idx, char in enumerate(s)}  # Step 1
        partitions = []
        
        start, end = 0, 0
        for i, char in enumerate(s):  # Step 2
            end = max(end, last_occurrence[char])  # Update the partition end
            if i == end:  # If current index reaches the end of partition
                partitions.append(end - start + 1)  # Store the partition length
                start = i + 1  # Move to the next partition
                
        return partitions

# Example usage
solution = Solution()
s = "ababcc"
print(solution.partitionLabels(s))  # Output: [4, 2]
