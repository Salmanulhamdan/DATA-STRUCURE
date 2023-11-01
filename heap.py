class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap)-1)

    def remove(self):
        if len(self.heap) > 1:
            min_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._bubble_down(0)
            return min_val
        elif len(self.heap) == 1:
            return self.heap.pop()
        return None

    def _bubble_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _bubble_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l < len(self.heap) and self.heap[l] < self.heap[min_index]:
            min_index = l
        r = self.right_child(i)
        if r < len(self.heap) and self.heap[r] < self.heap[min_index]:
            min_index = r
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._bubble_down(min_index)

    def build_heap(self, arr):
        n = len(arr)
        self.heap = arr[:]
        for i in range(n//2-1, -1, -1):
            self._bubble_down(i)

# Sample usage
heap = MinHeap()
heap.build_heap([4, 2, 8, 5, 1, 6])
print(heap.heap)
heap.insert(0)
print(heap.heap)
heap.remove()
print(heap.heap)
