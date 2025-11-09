from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from itertools import count

T = TypeVar('T')

class PriorityQueue(ABC, Generic[T]):
    """
    Abstract class priority queue, has all functions that a priority queue requires, so that they must be implemented
    ensures that things will be implemented correctly
    
    """
    @abstractmethod
    def build_queue(self, data:dict[T, float]) -> None:
        pass

    @abstractmethod
    def insert (self, key:T, priority:float):
        pass
    @abstractmethod
    def delete_min(self) -> T:
        pass
    @abstractmethod
    def decrease_key(self, key:T, priority:float):
        pass
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __bool__(self) -> bool:
        pass

class BinaryHeapPQ(PriorityQueue[T]):
    """
    Class for a Binary Heap Priority Queue
    This will hold a priority queue for all the data

    Attributes:
        T, the data type
        __indexes(dict[T, int]) The indexes of the queue, allows us to improve decrease key insertion time.
        __data(list[tuple[T, float]]) the queue, allows us to store data

    """
    __slots__ = ["__index","__data","__counter"]
    def __init__(self)-> None:
        self.__index:dict[T, int] = {}
        self.__data:list[tuple[float, int, T]] = []
        self.__counter:count = count()
    
    def build_queue(self, data:dict[T, float]) -> None:
        if not isinstance(data, dict):
            raise TypeError
        for key, priority in data.items():
            self.insert(key, priority)
    
    def _swap(self, i:int, j:int) -> None:
        n = len(self.__data)
        if i < 0:
            i += n
        if j < 0:
            j += n
        self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
        self.__index[self.__data[i][2]] = i
        self.__index[self.__data[j][2]] = j

        
    def _parent(self, index:int) -> int:
        return (index-1) // 2
    def _left(self, index:int) -> int:
        return(index * 2) + 1
    def _right(self, index:int) -> int:
        return(index * 2) + 2
    
    def _bubble_up(self, index:int) -> None:
        parent: int = self._parent(index)
        while index > 0 and self.__data[index] < self.__data[parent]:
            self._swap(index, parent)
            index = parent
            parent = self._parent(index)

    
    def insert(self, key:T, priority:float) -> None:
        self.__index[key] = len(self.__data)
        self.__data.append((priority, next(self.__counter), key))
        self._bubble_up(self.__index[key])

    def decrease_key(self, key:T, priority:float) -> None:
       
        if key not in self.__index.keys():
            raise ValueError
        _, order, _ = self.__data[self.__index[key]]
        self.__data[self.__index[key]] = (priority, order, key)
        self._bubble_up(self.__index[key])

    def _bubble_down(self, i:int) -> None:
        n:int = len(self.__data)
        while True:
            min_i:int = i
            l, r = self._left(i), self._right(i)  
            if l < n and self.__data[l] < self.__data[min_i]:
                min_i = l
            if r < n and self.__data[r] < self.__data[min_i]:
                min_i = r
            if min_i == i:
                break
            self._swap(i, min_i)
            i = min_i

    def delete_min(self) -> T:
        _, _, min_key = self.__data[0]
        last:tuple[float, int, T] = self.__data.pop()
        self.__index.pop(min_key)
        if self.__data:
            self.__data[0] = last
            self.__index[last[2]] = 0
            self._bubble_down(0)
        return min_key
    
    def __len__(self) -> int:
        return len(self.__data)
    def __bool__(self) -> bool:
        return bool(self.__data)
            



class LinearPQ(PriorityQueue[T]):
    """
    Class for a Linear Priority Queue
    This will hold a priority queue for all the data

    Attributes:
        T, the data type
        __data(dict[T, float]) the queue, allows us to store data

    """

    __slots__ = ["__data"]
    
    def __init__(self)-> None:
        self.__data:dict[T, float] = {}
    
    def build_queue(self, data:dict[T, float]) -> None:
        if not isinstance(data, dict):
            raise TypeError
        self.__data.update(data)

    def insert(self, key:T, priority:float) -> None:
        self.__data[key] = priority
    def decrease_key(self, key:T, priority:float) -> None:
        if key not in self.__data.keys():
            raise ValueError
        self.__data[key] = priority
    def delete_min(self) -> T:
        min_key:T = list(self.__data.keys())[0]
        min_value: float = self.__data[min_key]
        for cur_key, cur_value in self.__data.items():
            if min_value < cur_value:
                min_value = cur_value
                min_key = cur_key
        self.__data.pop(min_key)
        return min_key
    def __len__(self) -> int:
        return len(self.__data)
    def __bool__(self) -> bool:
        return bool(self.__data)