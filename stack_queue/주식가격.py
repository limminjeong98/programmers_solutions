def solution(prices):
    answer = [len(prices)-i-1 for i in range(len(prices))]
    stack = [0]
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            else:
                break
        stack.append(i)
    return answer