__all__ = ['CacheCalculator']
from lru_cache import LruCache
from calculation import Calculation

"""
    This class represents cache calculator

"""


class CacheCalculator(LruCache):

    def __init__(self, size: int):
        """

        :param size: the size of the cache
        """
        super().__init__(size)

    def calculate(self, left_side: int, right_side: int, operator: str):

        """

        :param left_side: the left side of the phrase
        :param right_side: the right side of the phrase
        :param operator: the action we want to perform on the phrase
        :return: a tuple of the  result of the phrase and where he is calculated

      """

        my_calculation = Calculation(right_side=right_side, left_side=left_side, operator=operator)
        if self.get(my_calculation.__str__()) is None:
            if operator == 'mul':
                self.put(my_calculation.__str__(),(left_side*right_side))
                p = (left_side*right_side, 'False')
                return p
            elif operator == 'sum':
                self.put(my_calculation.__str__(),left_side+right_side)
                p = (left_side+right_side, 'False')
                return p
            elif operator == 'sub':
                self.put(my_calculation.__str__(), left_side - right_side)
                p = (left_side - right_side, 'False')
                return p
            elif operator == 'div':
                if left_side == 0:
                    self.put(my_calculation.__str__(), 0)
                    p = (0, 'False')
                if right_side == 0:
                    p = (0, "division by zero is not allowed")
                    return p
                else:
                    self.put(my_calculation.__str__(), left_side / right_side)
                    p = (left_side / right_side, 'False')
                    return p

        else:
            p = (self.get(my_calculation.__str__()), f'True')
            return p

    def __str__(self):
        return super().__str__()



if __name__ == "__main__":
    my_calculator = CacheCalculator(size=3)
    my_calculator.calculate(left_side=4, right_side=3,  operator='mul')
    my_calculator.calculate(left_side=5, right_side=5, operator="sum")
    my_calculator.calculate(left_side=6, right_side=3, operator="sub")
    print(my_calculator)
    result, is_cached_used = my_calculator.calculate(left_side=4, right_side=3, operator='mul')
    print(result) # should print: 12
    print(is_cached_used) # should print: True
    result, is_cached_used = my_calculator.calculate(left_side=60, right_side=12, operator="div")
    print(result) # should print: 5
    print(is_cached_used) # should print: False
    print(my_calculator)




