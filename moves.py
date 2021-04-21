
def minMoves( nums: list[int]) -> int:
        m = ""
        for i in nums:
            if m == "":
                m = i
            else:
                m = min(m,i)
        moves = 0
        for i in nums:
            moves += i - m
        return moves

print(minMoves([1,2,3]))