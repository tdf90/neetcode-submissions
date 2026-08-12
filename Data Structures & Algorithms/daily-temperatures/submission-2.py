class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # As days are getting colder, we're accumulating values to previous days
        # As days get warmer, we hitting those previous days and checking them

        # iterate through the temperatures.
        # if it gets colder, add that day to a stack
        # if it gets warmer, pop from the stack until we hit the current val
        # each pop increments the days for that index.


        days_before_a_warmer_day = [0] * len(temperatures)

        stack = [] # keep just the indicies, we can look up temps
        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                days_before_a_warmer_day[prev_index] = i - prev_index

            stack.append(i)
                
            
        return days_before_a_warmer_day

