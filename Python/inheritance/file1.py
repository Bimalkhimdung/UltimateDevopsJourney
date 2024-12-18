class OTTsub():
    def __init__(self,id,name,plan):
        self.user_name = name
        self.user_id = id
        self.user_plan = plan 
    def subscribed(self):
        print(f"Subscriber with {self.user_id} id subscribed to the {self.user_plan} Plan")
    def unsubscribed(self):
        print(f"Subscriber with {self.user_id} id unsubscribed to the {self.user_plan} Plan")

#creating empty dictionary 
subscription = {}

# creating function to get user input 

def get_details():
    users_id = input("Please Enter your Subscription Id: ")
    users_name = input("Please Enter Your Name: ")
    users_plan = input("Please Enter your Plan (Monthly/Yearly): ")

#creating instance inside a function / object
    o_ = OTTsub(users_id, users_name, users_plan)

#ask user if want to subscribe or not 

    subscribe = input(" Do you want to upgrade the subscription?: ").strip().upper()

    if subscribe == "Y":
        o_.subscribed()
        subscription[users_id] = {'name': o_.user_name, 'plan':o_.user_plan}
        print(f"Subscription saved: { subscription[users_id]}")

    else:
        o_.unsubscribed()

get_details()
