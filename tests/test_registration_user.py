from automation_practice_form.model.pages.registration_page import RegistrationPage


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('yashaka')
    registration_page.fill_last_name('selene')
    registration_page.fill_email('yashaka@selene.com')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_phone('9876543210')
    registration_page.fill_date_of_birth('2005', 'April', '18')
    registration_page.select_hobbies('Reading')
    registration_page.fill_subjects('Arts')
    registration_page.upload_file('\\resources\\1.png')
    registration_page.fill_address('Address')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit_click()
    registration_page.should_registered_user_with('yashaka selene', 'yashaka@selene.com', 'Male', '9876543210',
                                                  '18 April,2005', 'Arts', 'Reading', '1.png',
                                                  'Address', 'NCR Delhi')
