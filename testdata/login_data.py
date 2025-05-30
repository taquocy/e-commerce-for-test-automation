login_test_cases = [
    {
        "case": "Valid admin login",
        "username": "admin1@gmail.com",
        "password": "admin1admin1",
        "expect_success": True
    },
    # {
    #     "case": "Valid user login",
    #     "username": "user0@gmail.com",
    #     "password": "user0user0",
    #     "expect_success": True
    # },
    {
        "case": "Invalid password",
        "username": "admin1@gmail.com",
        "password": "wrongpassword",
        "expect_success": False
    },
    {
        "case": "Invalid username",
        "username": "notfound@gmail.com",
        "password": "admin1admin1",
        "expect_success": False
    },
    {
        "case": "Empty username",
        "username": "",
        "password": "admin1admin1",
        "expect_success": False
    },
    {
        "case": "Empty password",
        "username": "admin1@gmail.com",
        "password": "",
        "expect_success": False
    }
]