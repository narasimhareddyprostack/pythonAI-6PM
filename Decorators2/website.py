from login import login_req

def home_page(status):
    print("Home Page")
@login_req
def order_page(status):
    print("Order Page")

@login_req
def product_page(status):
    print("product Page")

def contact_page(status):
    print("contact Page")

home_page(True)
order_page(False)
product_page(False)
contact_page(True)