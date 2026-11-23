import uuid
from dataclasses import dataclass, field

from faker import Faker

fake = Faker()


def generate_email() -> str:
    return f"test_{uuid.uuid4().hex[:8]}@example.com"


def random_dob() -> str:
    return fake.date_of_birth(minimum_age=18, maximum_age=75).isoformat()


@dataclass()
class User:
    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    dob: str = field(default_factory=random_dob)
    country: str = "United States of America (the)"
    postal_code: str = field(default_factory=fake.postalcode)
    house_number: str = field(default_factory=fake.building_number)
    street: str = field(default_factory=fake.street_name)
    city: str = field(default_factory=fake.city)
    state: str = field(default_factory=fake.state)
    phone: str = "9110987844"
    email: str = field(default_factory=generate_email)
    password: str = "Test123!@Test123!@"
