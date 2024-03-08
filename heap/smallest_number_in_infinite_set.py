'''
2336 smallest number in infinite set
'''
class SmallestInfiniteSet:
    def __init__(self) -> None:
        self.present = [True for _ in range(1001)]
        
    def popSmallest(self):
        for x in range(1,1001):
            if self.present(x):
                self.present[x] = False
                return x
    def addBack(self, nums):
        self.present(nums) = True