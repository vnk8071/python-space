# USER CLASS DEFINITION
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


# USER FUNCTIONS
def create_user(first_name, last_name, email, username, age, interests):
    """
    Function to create a user and print the user data.
    """
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "username": username,
        "age": age,
        "interests": interests,
    }
    print(user)


# USER EXAMPLE USAGE
create_user("Max", "Max", "test@test.com", "testers", 31, ["Sports", "Cooking"])


# USER CLASS WITH SESSION AND SAVE METHODS
class User:
    def create_session(self):
        print("Session created")

    def save(self):
        print("User saved to the database")


# USER CLASS EXAMPLE USAGE
user = User()
user.create_session()
user.save()

# EMAIL VALIDATION FUNCTION
import re


def is_valid_email(email):
    """
    Function to check if an email is valid using a regular expression.
    """
    email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return bool(email_regex.match(email))


# EMAIL VALIDATION EXAMPLE USAGE
email = "test@example.com"
if is_valid_email(email):
    print("Email is valid")
else:
    print("Invalid email")

# FILE WRITING EXAMPLE
with open("example.txt", "w") as file:
    data = "Hello, this is some data to be written to the file."
    file.write(data)


# LOGIN FUNCTION AND EXAMPLE USAGE
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


def login(email, password):
    user_list = [User("test@test.com", "testers")]

    for user in user_list:
        if user.email == email and user.password == password:
            print("Login successful")
            return

    print("Invalid credentials")


email = "test@test.com"
password = "testers"
login(email, password)


# PRODUCT CLASS AND CREATION FUNCTION
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def create_product(name, price):
    product = Product(name, price)
    print(f"Product {product}: '{name}' created with price ${price}")


# PRODUCT CREATION EXAMPLE USAGE
create_product("Carpet", 12.99)


# USER CLASS WITH SESSION AND SAVE METHODS (REPEATED FOR CLARITY)
class User:
    def create_session(self):
        print("Session created")

    def save(self):
        print("User saved to the database")


# USER CLASS EXAMPLE USAGE (REPEATED FOR CLARITY)
user = User()
user.create_session()
user.save()


# RECTANGLE CLASS AND CREATION FUNCTION
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def create_rectangle(x, y, width, height):
    rectangle = Rectangle(x, y, width, height)
    print(
        f"Rectangle {rectangle} created: X={x}, Y={y}, Width={width}, Height={height}"
    )


# RECTANGLE CREATION EXAMPLE USAGE
create_rectangle(10, 9, 30, 12)


# USER CLASS AND CREATION FUNCTION
class User:
    def __init__(self, email, age, username):
        self.email = email
        self.age = age
        self.username = username


def create_user(email, age, username):
    user = User(email, age, username)
    print(f"User {user} created: Email={email}, Age={age}, Username={username}")


# USER CREATION EXAMPLE USAGE
create_user("test@test.com", 31, "max")


# RECTANGLE CLASS AND CREATION FUNCTION (USING DICTIONARY UNPACKING)
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def create_rectangle(properties):
    rectangle = Rectangle(**properties)
    print(
        f"Rectangle created: X={rectangle.x}, Y={rectangle.y}, Width={rectangle.width}, Height={rectangle.height}"
    )


# RECTANGLE CREATION EXAMPLE USAGE (USING DICTIONARY UNPACKING)
rectangle_properties = {"x": 10, "y": 9, "width": 30, "height": 12}
create_rectangle(rectangle_properties)


# DATABASE CLASS AND LOGIN FUNCTION
class Database:
    def find(self, table, field, operator, value):
        users = [
            {"email": "user1@example.com", "password": "password1"},
            {"email": "user2@example.com", "password": "password2"},
            # ... other user data
        ]

        for user in users:
            if user[field] == value:
                return user

        return None


def login(email, password, database):
    if "@" not in email or len(password) < 7:
        raise ValueError("Invalid input!")

    existing_user = database.find("users", "email", "==", email)

    if not existing_user:
        raise ValueError("Could not find a user for the provided email.")

    if existing_user["password"] == password:
        print("Session created")
    else:
        raise ValueError("Invalid credentials!")


# LOGIN EXAMPLE USAGE
database = Database()
try:
    login("user1@example.com", "password1", database)
except ValueError as e:
    print(e)


# USER CLASS WITH PASSWORD VALIDATION
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_password(self, provided_password):
        if self.password != provided_password:
            raise ValueError("Invalid credentials!")


# USER INPUT VALIDATION FUNCTION
def validate_user_input(email, password):
    if "@" not in email or len(password) < 7:
        raise ValueError("Invalid input!")


# FIND USER BY EMAIL FUNCTION
def find_user_by_email(email):
    users = [
        User("user1@example.com", "password1"),
        User("user2@example.com", "password2"),
        # ... other user data
    ]

    for user in users:
        if user.email == email:
            return user

    return None


# LOGIN FUNCTION WITH USER CLASS
def login(email, password):
    validate_user_input(email, password)
    existing_user = find_user_by_email(email)

    if not existing_user:
        raise ValueError("Could not find a user for the provided email.")

    existing_user.validate_password(password)


# LOGIN EXAMPLE USAGE WITH USER CLASS
try:
    login("user1@example.com", "password1")
except ValueError as e:
    print(e)


# DATABASE CLASS DEFINITION
class Database:
    def __init__(self, uri):
        self.uri = uri

    def connect(self):
        """
        Method to connect to the database.
        """
        # Replace this line with your actual database connection logic
        print(f"Connected to database with URI: {self.uri}")


# DATABASE CONNECTION FUNCTION
def connect_to_database(uri):
    """
    Function to connect to the database using the Database class.
    """
    if uri == "":
        print("Invalid URI!")
        return

    db = Database(uri)
    db.connect()


# Example usage
connect_to_database("your_database_uri_here")

# URI VALIDATION FUNCTION
import re


def uri_is_valid(uri):
    """
    Function to check if a URI is valid using a regular expression.
    """
    uri_regex = re.compile(r"^[a-zA-Z]+://[^\s]+$")
    return bool(uri_regex.match(uri))


# ERROR DISPLAY FUNCTION
def show_error(message):
    """
    Function to display an error message.
    """
    print(f"Error: {message}")


# DATABASE CONNECTION FUNCTION WITH URI VALIDATION
def connect_to_database(uri):
    """
    Function to connect to the database with URI validation.
    """
    if not uri_is_valid(uri):
        show_error("Invalid URI!")
        return

    db = Database(uri)
    db.connect()


# Example usage
connect_to_database("your_database_uri_here")


# USER CLASS DEFINITION
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


# USER INPUT VALIDATION FUNCTION
def validate_user_input(email, password):
    """
    Function to validate user input (email and password).
    """
    if "@" not in email or len(password) < 7:
        raise ValueError("Invalid input!")


# CREDENTIALS VERIFICATION FUNCTION
def verify_credentials(email, password):
    """
    Function to verify user credentials.
    """
    user = find_user_by_email(email)

    if user is None or user.password != password:
        raise ValueError("Invalid credentials!")


# SESSION CREATION FUNCTION
def create_session():
    """
    Function to create a user session.
    """
    print("Session created")


# FIND USER BY EMAIL FUNCTION
def find_user_by_email(email):
    """
    Function to find a user by email.
    """
    users = [
        User("user1@example.com", "password1"),
        User("user2@example.com", "password2"),
        # ... other user data
    ]

    for user in users:
        if user.email == email:
            return user

    return None


# LOGIN FUNCTION
def login(email, password):
    """
    Function to perform user login.
    """
    validate_user_input(email, password)
    verify_credentials(email, password)
    create_session()


# Example usage
try:
    login("user1@example.com", "password1")
    # If login is successful, continue with the application logic
except ValueError as e:
    print(e)


# USER CLASS DEFINITION (REPEATED FOR CLARITY)
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


# INPUT VALIDATION FUNCTION
def input_invalid(email, password):
    """
    Function to check if user input is invalid.
    """
    return "@" not in email or len(password) < 7


# ERROR DISPLAY FUNCTION
def show_error(email, password):
    """
    Function to display an error message for invalid input.
    """
    print(f"Error: Invalid input! Email: {email}, Password: {password}")


# CREDENTIALS VERIFICATION AND SESSION CREATION FUNCTIONS (REPEATED FOR CLARITY)
def verify_credentials(email, password):
    """
    Function to verify user credentials.
    """
    user = find_user_by_email(email)

    if user is None or user.password != password:
        show_error(email, password)
        return

    create_session()


def create_session():
    """
    Function to create a user session.
    """
    print("Session created")


# FIND USER BY EMAIL FUNCTION (REPEATED FOR CLARITY)
def find_user_by_email(email):
    """
    Function to find a user by email.
    """
    users = [
        User("user1@example.com", "password1"),
        User("user2@example.com", "password2"),
        # ... other user data
    ]

    for user in users:
        if user.email == email:
            return user

    return None


# EXAMPLE USAGE WITH INPUT VALIDATION
email = "user1@example.com"
password = "password1"

if input_invalid(email, password):
    show_error(email, password)
else:
    verify_credentials(email, password)


# User class definition
class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name

    def save(self):
        print(f"User {self.user_id} updated - Name: {self.name}, Age: {self.age}")


# Function to validate user data
def validate_user_data(user_data):
    if "id" not in user_data or "name" not in user_data or "age" not in user_data:
        raise ValueError("Invalid user data!")


# Function to find a user by ID
def find_user_by_id(user_id):
    users = [
        User(1, "John Doe", 30),
        User(2, "Jane Doe", 25),
        # ... other user data
    ]

    for user in users:
        if user.user_id == user_id:
            return user

    return None


# Function to apply user data updates
def apply_update(user_data):
    user = find_user_by_id(user_data["id"])

    if user is not None:
        user.set_age(user_data["age"])
        user.set_name(user_data["name"])
        user.save()
    else:
        raise ValueError(f"User with ID {user_data['id']} not found.")


# Function to update a user
def update_user(user_data):
    validate_user_data(user_data)
    apply_update(user_data)


# Example usage
user_data = {"id": 1, "name": "Updated Name", "age": 35}

try:
    update_user(user_data)
except ValueError as e:
    print(e)


# Transaction class definition
class Transaction:
    def __init__(self, transaction_type, amount):
        self.type = transaction_type
        self.amount = amount


# Function to validate a transaction
def validate_transaction(transaction):
    if transaction.type == "UNKNOWN":
        raise ValueError("Invalid transaction type.")


# Function to check if a transaction is a payment
def is_payment(transaction):
    return transaction.type == "PAYMENT"


# Function to process a payment transaction
def process_payment(transaction):
    print(f"Processing payment transaction with amount: {transaction.amount}")


# Function to process a transaction
def process_transaction(transaction):
    validate_transaction(transaction)

    if is_payment(transaction):
        process_payment(transaction)
    # Add more conditions for other transaction types if needed


# Example usage
transaction_data = {"type": "PAYMENT", "amount": 100}

try:
    transaction = Transaction(transaction_data["type"], transaction_data["amount"])
    process_transaction(transaction)
except ValueError as e:
    print(e)


# User class definition (repeated for clarity)
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        print(f"User saved - Email: {self.email}, Password: {self.password}")


# Function to validate user input
def validate_user_input(email, password):
    if not is_email(email) or password_is_invalid(password):
        raise ValueError("Invalid input!")

    create_session()


# Function to check if an email is valid
def is_email(email):
    return "@" in email


# Function to check if a password is invalid
def password_is_invalid(password):
    return len(password) < 8


# Function to create a user session
def create_session():
    print("Session created")


# Example usage
user_data = {"email": "test@example.com", "password": "securepassword"}

try:
    validate_user_input(user_data["email"], user_data["password"])
except ValueError as e:
    print(e)
