from datastructures.deque import Deque
from datastructures.array import Array

class Bistro_System:
    
    def __init__(self) -> None:
        open_orders = Deque()
        finished_orders = Array()