from connection import Customer,session


# create

# def create_customer(name,email):
#     session.add(Customer(cust_name=name,cust_email=email))
#     session.commit()


# create_customer('Vamshi','vamshi@gmail.com')
# create_customer('Venkatesh','venkatesh@gmail.com')
# create_customer('Rohit','rohit@gmail.com')
# create_customer('Sidhartha','sidhartha@gmail.com')
# create_customer('Noel','noel123@gmail.com')


# read

# def read_all():
#     customers = session.query(Customer).all()
#     for customer in customers:
#         print(customer.cust_name,customer.cust_email)

# read_all()


# read one 

# def read_one(id):
#     customer = session.query(Customer).filter(Customer.cust_id==id).first()
#     print(customer)

# read_one(1)

# update 

# def update_email(id,new_email):
#     customer = session.query(Customer).filter(Customer.cust_id==id).first()
#     customer.cust_email = new_email
#     session.commit()

# update_email(2,"VENKATESH@gmail.com")


delete 
def delete_customer(id):
    customer = session.query(Customer).filter(Customer.cust_id==id).first()
    session.delete(customer)
    session.commit()

delete_customer(2)