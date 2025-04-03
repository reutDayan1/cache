__all__ = ['Calculation']

from enum import Enum


class Operator(Enum):
    mul = 'mul'
    sum = 'sum'
    div = 'div'
    sub = 'sub'


class Calculation:
    """
        This class represents calculation.

    """

    def __init__(self,left_side: int, right_side: int, operator: str):
        """

        :param left_side: the left side of the phrase
        :param right_side: the right side of the phrase
        :param operator: the action we want to perform on the phrase
        """
        self._left_side = left_side
        self._right_side = right_side
        self._operator = operator

    def __str__(self) -> str:
        """

        :return:  calculate of the phrase on str
        """

        if self._operator == Operator.mul.name:
            return str(self.mul())
        elif self._operator == Operator.sum.name:
            return str(self.sum())
        elif self._operator == Operator.sub.name:
            return str(self.sub())
        elif self._operator == Operator.div.name:
            return str(self.div())

    def sum(self) -> str:
        """
        :return: the sum of the phrase
        """
        return f'{self._left_side}+{self._right_side}'

    def sub(self) -> str:
        """

        :return: the subtraction of the phrase
        """
        return f'{self._left_side}-{self._right_side}'

    def mul(self) -> str:
        """

        :return: the multiplication of the phrase
        """
        return f'{self._left_side}*{self._right_side}'

    def div(self) -> str:
        """

        :return: the division of the phrase
        """
        return f'{self._left_side}/{self._right_side}'






if __name__ == "__main__":
    op = 'mul'
    my_calculation = Calculation(3,5,op)
    print(my_calculation)
    my_calculation1=Calculation(3,5,op)
    print(my_calculation1)
    my_calculation2 = Calculation(3, 5, op)
    print(my_calculation2)
    my_calculation12 = Calculation(3, 5, op)
    print(my_calculation12)
