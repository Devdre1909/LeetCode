class Solution:
    def isHappy(self, n):
        count = 0
        is_previous = []
        number = self.splitNConvert(n)
        while True:
            print(number)
            sum = 0
            count = count + 1
            for num in number:
                sum = sum + num ** 2
            if (sum == 1):
                return True
            else:
                if (sum in is_previous):
                    return False
                is_previous.append(sum)
                number = self.splitNConvert(sum)

    def splitNConvert(self, n):
        return [int(num) for num in list(str(n))]


print(Solution().isHappy(101))
