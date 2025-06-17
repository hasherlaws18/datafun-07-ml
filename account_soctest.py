from decimal import Decimal

class Account:
    """
    Account class for demonstrating doctest.
    """

    def __init__(self, name, balance):
        """
        Initialize an Account object.

        >>> account1 = Account('John Green', Decimal('50.00'))
        >>> account1.name
        'John Green'
        >>> account1.balance
        Decimal('50.00')

        The balance argument must be greater than or equal to 0.
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
        ...
        ValueError: Initial balance must be greater than or equals to to 0.00.
        """
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be greater than or equals to to 0.00.')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money to the account.

        >>> acc = Account('Jane Doe', Decimal('100.00'))
        >>> acc.deposit(Decimal('25.00'))
        >>> acc.balance
        Decimal('125.00')
        """
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
        self.balance += amount

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
