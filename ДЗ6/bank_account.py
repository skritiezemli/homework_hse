class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self.operations_history = []

    def create_operation(self, type, count):
        """Создание словаря с информацией об операции"""
        operation = {
            "name": self.name,
            "type": type,
            "count": count,
            "balance": self.start_balance,
        }
        return operation

    def put_money(self, count):
        """
        Добавление денег на банковский счет
        """
        self.start_balance += count

        operation = self.create_operation("внесено", count)
        self.operations_history.append(operation)
        print(
            f"{self.name} внесено {count} рублей. Текущий баланс: {self.start_balance}"
        )

    def take_money(self, count):
        """
        Снятие денег со счета
        """
        if count <= 0:
            print("Недостаточно средств на счете")
            return
        self.start_balance -= count
        operation = self.create_operation("снято", count)
        self.operations_history.append(operation)
        print(f"{self.name} снято {count} рублей. Текущий баланс: {self.start_balance}")

    def get_history(self):
        """
        Вывод истории операций
        """
        return self.operations_history


account1 = Account("Иван", 100)
account1.put_money(50)
account1.take_money(20)
history = account1.get_history()
print(history)
