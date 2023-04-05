import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_phone: str
    date_of_birth: tuple
    hobbies: str
    subjects: str
    upload_file: str
    address: str
    state: str
    city: str
