"""arithmetic module
"""

class Calculator:
    """Calculator class
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add(self, x: int, y: int) -> int:
        """add two numbers

        Parameters
        ----------
        x : int
            left number
        y : int
            right number

        Returns
        -------
        int
            sum of two numbers
        """

        return x+y


    def sub(self, x: int, y: int) -> int:
        """subtract two numbers

        Parameters
        ----------
        x : int
            left number
        y : int
            right number

        Returns
        -------
        int
            minus of two numbers
        """

        return x-y