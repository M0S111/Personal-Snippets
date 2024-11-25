def BalancedBrax(string):
    # Initialize a stack to keep track of opening brackets
    stack = []

    for idx, char in enumerate(string):
        if char in '([{':
            stack.append((char, idx))  # Store both the bracket and its index
        elif char in ')]}':
            # Check if the stack is empty (no matching opening bracket)
            if not stack:
                return idx + 1  # Unmatched closing bracket
            last_opening, last_opening_idx = stack.pop()
            # Determine the expected opening bracket for the current closing bracket
            expected_opening = {'}': '{', ']': '[', ')': '('}.get(char)
            if last_opening != expected_opening:
                return idx + 1  # Unmatched closing bracket

    # Check if any opening brackets are unmatched
    if stack:
        return (stack[-1][1])+1  # Unmatched opening bracket index
    return 'Success'

print(BalancedBrax('([{}])'))
