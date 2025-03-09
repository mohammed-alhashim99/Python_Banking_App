import csv


class Account:
    def __init__(self, account_id, first_name, last_name, password, balance_checking, balance_savings):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings

    def list_acc(self):
        list_of_acc = [
            f"{self.account_id};{self.first_name};{self.last_name};{self.password};{self.balance_checking};{self.balance_savings}"]
        with open('bank.csv', mode='a', newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(list_of_acc)
        return list_of_acc
    

user = Account(1000,"mohammed","ah","pou776",2500,6333)
print(user.list_acc())

# class Withdraw(Account):
#     pass
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
