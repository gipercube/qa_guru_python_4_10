import os

from selene import have, command
from selene.support.shared import browser
from datetime import datetime


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('[for="gender-radio-1"]')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.date_of_birth_year = browser.element('.react-datepicker__year-select')
        self.date_of_birth_month = browser.element('.react-datepicker__month-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobbies = browser.element('[for="hobbies-checkbox-2"]')
        self.upload_picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.state_select = browser.element('#react-select-3-option-0')
        self.city = browser.element('#city')
        self.city_select = browser.element('#react-select-4-option-0')
        self.submit = browser.element('#submit')

    def fill_registration_form(self, user):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.select_gender(user.gender)
        self.fill_mobile_phone(user.mobile_phone)
        self.fill_date_of_birth(*user.date_of_birth)
        self.select_hobbies(user.hobbies)
        self.fill_subjects(user.subjects)
        self.upload_file(f'\\resources\\{user.upload_file}')
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit_click()

    def open(self):
        browser.open('/automation-practice-form')
        browser.config.driver.maximize_window()
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def select_gender(self, value):
        self.gender.should(have.text(f'{value}')).click()
        return self

    def fill_mobile_phone(self, value):
        self.user_number.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.date_of_birth_month.type(month)
        self.date_of_birth_year.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def select_hobbies(self, value):
        self.hobbies.should(have.text(value)).click()
        return self

    def fill_subjects(self, value):
        self.subjects_input.type(f'{value}').press_enter()
        return self

    def upload_file(self, value):
        self.upload_picture.send_keys(os.getcwd() + value)
        return self

    def fill_address(self, value):
        self.address.type(value)

    def select_state(self, value):
        self.state.click()
        self.state_select.should(have.text(f'{value}')).click()
        return self

    def select_city(self, value):
        self.city.click()
        self.city_select.should(have.text(f'{value}')).click()
        return self

    def submit_click(self):
        self.submit.click()
        return self

    def should_registered_user_with(self, user):
        full_name = f'{user.first_name} {user.last_name}'
        state_and_city = f'{user.state} {user.city}'
        dateofbirthday = str(datetime.strptime(' '.join(user.date_of_birth), '%Y %B %d').strftime('%d %B,%Y'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user.email,
                user.gender,
                user.mobile_phone,
                dateofbirthday,
                user.subjects,
                user.hobbies,
                user.upload_file,
                user.address,
                state_and_city
            )
        )
        return self
