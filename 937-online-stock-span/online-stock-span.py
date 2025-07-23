class StockSpanner:

    def __init__(self):
        self.mono_stack = []  # Each element is (price, span)

    def next(self, price: int) -> int:
        span = 1

        # Pop all smaller prices and accumulate their spans
        while self.mono_stack and self.mono_stack[-1][0] <= price:
            span += self.mono_stack.pop()[1]

        self.mono_stack.append((price, span))  # Push current price and span
        return span
