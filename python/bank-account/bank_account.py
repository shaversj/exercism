import threading


class BankAccount:
    def __init__(self):
        self.balance_lock = threading.Lock()

    def get_balance(self):
        if self.is_open:
            return self.balance
        else:
            raise ValueError("The account is closed.")

    def open(self):

        try:
            self.is_open
            if self.is_open is False:
                raise AttributeError("Re-open a previously closed account.")
            else:
                raise ValueError("An account has already been opened.")
        except AttributeError:
            self.balance = 0
            self.is_open = True

        return self.balance, self.is_open

    def deposit(self, amount):
        if self.is_open:
            self.balance_lock.acquire()
            self.balance = self.balance + amount
            self.balance_lock.release()
            if amount < 0:
                raise ValueError("Can not deposit a negative amount to account.")
        else:
            raise ValueError("You can not deposit funds into a closed account.")

        return self.balance

    def withdraw(self, amount):
        if self.is_open:
            self.balance_lock.acquire()
            self.balance = self.balance - amount
            self.balance_lock.release()
            if amount < 0:
                raise ValueError("Can not withdraw a negative amount from account.")
            if self.balance < 0:
                raise ValueError(
                    "Transaction can not be completed due to insufficient funds."
                )

        else:
            raise ValueError("You can not withdraw funds from a closed account.")

        return self.balance

    def close(self):
        if self.is_open is False:
            raise ValueError("Account has already been closed.")
        else:
            self.is_open = False

        return self.is_open
