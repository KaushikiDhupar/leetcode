class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        res = set()
        set_b = set(b)  # Convert list b to a set for O(1) lookup
        for num in a:
            if num in set_b:
                res.add(num)  # Use a set to avoid duplicates
        return list(res)  # Convert set to list before returning
