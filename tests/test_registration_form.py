from automation_practice_form.model.pages.registration_page import RegistrationPage
from automation_practice_form.data.users import User


def test_registration_user():
    # GIVEN
    yasha = User(
        first_name='yashaka',
        last_name='selene',
        email='yashaka@selene.com',
        gender='Male',
        mobile_phone='9876543210',
        date_of_birth=('2005', 'April', '18'),
        hobbies='Reading',
        subjects='Arts',
        upload_file='1.png',
        address='Address',
        state='NCR',
        city='Delhi'
    )
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_registration_form(yasha)

    # THEN
    registration_page.should_registered_user_with(yasha)
