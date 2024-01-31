class UserData:
    def __init__(self):
        self.name = ""
        self.age = 0


user_data = UserData()
user_data.name = "KhoiVN"
user_data.age = 24


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")


user_instance = User("KhoiVN", 24)
user_instance.greet()


class Logistics:
    @staticmethod
    def issue_delivery(product, delivery_type):
        print(f"Delivering {product} by {delivery_type} delivery")

    @staticmethod
    def track_delivery(product, delivery_type):
        print(f"Tracking {product} by {delivery_type} delivery")


class Delivery:
    def __init__(self, purchase):
        self.purchase = purchase

    def deliver_product(self):
        Logistics.issue_delivery(self.purchase["product"], self.purchase.delivery_type)

    def track_product(self):
        Logistics.track_delivery(self.purchase["product"], self.purchase.delivery_type)


class ExpressDelivery(Delivery):
    def deliver_product(self):
        Logistics.issue_delivery(self.purchase["product"], "express")

    def track_product(self):
        Logistics.track_delivery(self.purchase["product"], "express")


class InsuredDelivery(Delivery):
    def deliver_product(self):
        Logistics.issue_delivery(self.purchase["product"], "insured")

    def track_product(self):
        Logistics.track_delivery(self.purchase["product"], "insured")


class StandardDelivery(Delivery):
    def deliver_product(self):
        Logistics.issue_delivery(self.purchase["product"], "standard")

    def track_product(self):
        Logistics.track_delivery(self.purchase["product"], "standard")


def create_delivery(purchase):
    if purchase["delivery_type"] == "express":
        return ExpressDelivery(purchase)
    elif purchase["delivery_type"] == "insured":
        return InsuredDelivery(purchase)
    else:
        return StandardDelivery(purchase)


express_delivery = create_delivery({"delivery_type": "express", "product": ...})
express_delivery.deliver_product()
