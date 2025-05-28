class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    
    def __repr__(self):
        return f"({self.value}, {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def insert(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_node = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_node
    
    def peek(self):
        return self.heap[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent_index].priority:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            
            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            
            if largest == index:
                break
            
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest
    
    def __repr__(self):
        return str(self.heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("A", 5)
    pq.insert("B", 3)
    pq.insert("C", 8)
    pq.insert("D", 8)
    
    print("Черга після вставок:", pq)
    print("Максимальний елемент:", pq.extract_max())
    print("Черга після видалення:", pq)
