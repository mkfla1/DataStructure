from heapq import heappush, heappop

class Heap:
    def __init__(self):
        self.minHeap = []
        self.deleted_index = set()
    
    def push(self, val, index):
        heappush(self.minHeap, (val, index))
    
    def _lazy_delete(self):
        while self.minHeap and self.minHeap[0][1] in self.deleted_index:
            self.deleted_index.remove(self.minHeap[0][1])
            heappop(self.minHeap)
    
    def delete_by_index(self, index):
        self.deleted_index.add(index)
    
    def top(self):
        self._lazy_delete()
        return self.minHeap[0]