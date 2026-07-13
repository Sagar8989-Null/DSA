class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        digits = "123456789"
        result = []

        min_length = len(str(low))
        max_length = len(str(high))

        for length in range(min_length, max_length + 1):
            for i in range(0, 10 - length):
                number = int(digits[i:i + length])

                if number >= low and number <= high:
                    result.append(number)

        return result