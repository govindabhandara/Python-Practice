class Account():
    min_bal=500
    def __init__(self,id,name):
        pass

    def open_account(self):
        self.acc_bal=200
    
    @classmethod
    def get_min_bal(cls):
        pass

    @staticmethod
    def cal_interest():
        tax=5

Account(101,"rahul")