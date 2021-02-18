class Testing():
    def singleNum(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a

example = Testing()
print(example.singleNum([2,2,1]))