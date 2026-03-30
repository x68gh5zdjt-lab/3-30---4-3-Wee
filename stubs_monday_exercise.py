import os
import random
from datetime import datetime


# ------------------------------------------------------------
# Exercise 1 -- datetime dependency
# ------------------------------------------------------------

def get_store_status(current_time=None):
    if current_time is None:
        current_time = datetime.now()

    hour = current_time.hour
    if 9 <= hour < 21:
        return "Store is open"
    else:
        return "Store is closed"


def test_store_open():
    fake_time = datetime(2025, 1, 1, 15, 0, 0)
    result = get_store_status(fake_time)
    assert result == "Store is open"


def test_store_closed_morning():
    fake_hour = datetime(2025, 1, 1, 8, 0, 0)
    result = get_store_status(fake_hour)
    assert result == "Store is closed"


def test_store_closed_night():
    fake_moment = datetime(2025, 1, 1, 23, 0, 0)
    result = get_store_status(fake_moment)
    assert result == "Store is closed"

# I realise now i could have just done a else statment 

# ------------------------------------------------------------
# Exercise 2 -- random dependency
# ------------------------------------------------------------

def assign_study_group(random_choice=None):
    if random_choice is None:
        random_choice = random.choice

    return random_choice(["Group A", "Group B", "Group C"])


def test_assign_study_group(): # i had to google stuff for this area, idk what im doing :sob: 
    def fake_choice(options):
        return "Group B"

    result = assign_study_group(fake_choice)
    assert result == "Group B"


# ------------------------------------------------------------
# Exercise 3 -- environment variable dependency
# ------------------------------------------------------------

def get_api_url(env=None):
    if env is None:
        env = os.getenv("APP_ENV")

    if env == "production":
        return "https://api.example.com"
    else:
        return "https://staging.example.com"


def test_api_url_production():
    result = get_api_url("production")
    assert result == "https://api.example.com"


def test_api_url_staging():
    result = get_api_url("staging")
    assert result == "https://staging.example.com"
