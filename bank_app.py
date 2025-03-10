import csv


class Account:
    last_id = 1000

    def __init__(self, first_name, last_name, password, balance_checking, balance_savings):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings

    def list_acc(self):
        list_of_acc = [
            self.account_id, self.first_name, self.last_name, self.password, self.balance_checking,
            self.balance_savings]
        with open('bank.csv', mode='a',newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(list_of_acc)
        return list_of_acc

    def save_to_csv(self):
        with open('bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.account_id,
                self.first_name,
                self.last_name,
                self.password,
                self.balance_checking,
                self.balance_savings
            ])
            
    def login(self, user_name, password_user):
        if user_name == self.account_id and password_user == self.password:
            return "successfully log in"
        else:
            return "try agin"


class Withdraw(Account):
    def __init__(self, account):
        super().__init__(account.first_name, account.last_name, account.password, account.balance_checking,
                         account.balance_savings)

    def withdraw_money(self, amount):
        if not self.login(self.account_id, self.password):
            return "Please log in first"

        if amount > self.balance_checking:
            return "Insufficient funds"

        self.balance_checking -= amount
        self.save_to_csv()
        return f"Withdrawal successful. New balance: {self.balance_checking}"

    def withdraw_from_savings(self, amount):
        if not self.login(self.account_id, self.password):
            return "Please log in first"
        if amount > self.balance_savings:
            return "Insufficient funds"

        self.balance_savings -= amount
        self.save_to_csv()
        return f"Withdrawal successful. New balance: {self.balance_savings}"


account1 = Account('mohammed', 'ahmed', 'juagw362', 1000, 10000)
print(account1.login(account1.account_id, 'juagw362'))

withdraw1 = Withdraw(account1)
print(withdraw1.withdraw_money(500))
print(withdraw1.withdraw_from_savings(600))
print(account1.list_acc())

#
#
# class Deposit(Account):
#     pass
#
#
# class Transfer(Account):
#     pass
#
#
# class Protection(Account):
#     pass
