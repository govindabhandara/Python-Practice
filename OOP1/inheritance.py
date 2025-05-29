class OTTSubscriptions():
    def __init__(self,sub_id,plan,tot_payment):
        self.id=sub_id
        self.plan=plan
        self.payment=tot_payment
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribe to the {self.plan}")

    def unsubscribe(self):
        print(f"Subscriber with {self.id} id unsubscribe to the {self.plan}")

netfilix=OTTSubscriptions(12021,"Monthly",100)
netfilix.plan
netfilix.subscribe()

class PremiumSubscription(OTTSubscriptions):
    def __init__(self, sub_id, plan, tot_payment,screen):
        super().__init__(sub_id, plan, tot_payment) 
        # self.id=sub_id
        # self.plan=plan
        # self.payment=tot_payment
        self.max_screen=screen
    # def subscribe(self):
    #     print(f"Subscriber with {self.id} id subscribe to the {self.plan}")

    # def unsubscribe(self):
    #     print(f"Subscriber with {self.id} id unsubscribe to the {self.plan}")

    def set_max_screen(self,screen):
        self.max_screen=screen
        print(f"Maximum screen set to {self.max_screen} in premium plan")
#no need to duplicacy
myott=PremiumSubscription("1233554","Monthly",1,1200)
myott.set_max_screen(1)