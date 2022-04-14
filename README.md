## E-comm API

AN e-Commerce API for faux projects. This project is built with the intention of aiding CS college students in their final year, looking for an e-commerce API with minimal functionalities (such as: creating users -as *sellers* or *customers*-, creating products and a comment system) with full CRUD capabilities. While you get these functions, it is a *soft* introduction to **Django REST framework**, as well as utilizing Django **AbstractBaseUser** for User creation.


![Create Product Owner](/imgs_show/create_seller.png "Product Owner Create")

![View Sellers (postman)](/imgs_show/postman.png "View sellers")

___

### How to Use
- *Fork this project*
- clone repository, and enter directory
- CMD: ```py manage.py makemigrations``` -> ```py manage.py migrate``` -> ```py manage.py runserver```
- Access endpoints (As seen below)
  



### ENDPOINTS (Localhost, for now) - ([live link here: ](https://e-commx.herokuapp.com/swagger/) DB not migrated yet)
___
##### ACCOUNTS:
{{domain}}: http://127.0.0.1:8000/api/accounts 

    {{domain}}/login: Authenticate user by generating a JWT token from email and password
    {{domain}}/login/refresh: Refresh ACCESS TOKEN generated from LOGIN
    {{domain}}/register/customer: Register Customer user to DB
    {{domain}}/register/seller: Register Seller user to DB
    {{domain}}/customers: View all customers
    {{domain}}/sellers: View all sellers
    {{domain}}/rate: Rate a Seller (a bit unconventional to be under Accounts)
    {{domain}}/sellers/ratings/all: View all ratings.

##### COMMENTS:
    Null

##### SERVICES:
{{domain}}: http://127.0.0.1:8000/api/services 

    {{domain}}/sellers: View all Sellers
    {{domain}}/products: View all Products and corresponding info (Also, CREATE product)
    {{domain}}/product/<int:pk>: View a particular Product by ID (Also, update product)