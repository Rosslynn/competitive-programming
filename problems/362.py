from collections import deque

class HitCounter:

    def __init__(self):
        self.dq = deque() 
        
    def hit(self, timestamp: int) -> None:
        self.dq.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        while self.dq and timestamp - self.dq[0] >= 300:
            self.dq.popleft()
        
        return len(self.dq)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)