from django.test import TestCase
from django.urls import reverse, resolve
from users.models import CustomUser
from users.forms import RegisterForm
from users.tests.factory_user import UserFactory
# from django.contrib.auth import get_user_model
from faker import Factory


faker = Factory.create()

# # Create your tests here.


class RegisterViewTest(TestCase):

    def setUp(self):
        # self.user = UserFactory()
        pass

    def test_register_success(self):

        register_url = reverse("register")
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        response = self.client.post(register_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response)
        self.assertRedirects(response, reverse('login'))

    def test_register_fail_email_field_is_blank(self):

        data = {
            'email': '',
            'password': faker.password(),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['email'].errors, ['Enter a valid email address.'])

    def test_register_fail_email_field_has_text(self):

        data = {
            'email': faker.text(10),
            'password': faker.password(),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['email'].errors, ['Enter a valid email address.'])

    def test_register_fail_email_already_exists(self):

        test_user = UserFactory()
        data = {
            'email': test_user.email,
            'password': faker.password(),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(CustomUser.objects.filter(
            email=data['email']).exists())
        self.assertTrue(form['email'].errors, ['Entered email address already exists.'])

    def test_register_fail_password_field_is_blank(self):

        data = {
            'email': faker.email(),
            'password': '',
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, ['Enter a valid password.'])

    def test_register_fail_password_field_has_text(self):

        data = {
            'email': faker.email(),
            'password': faker.text(10),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, [
                        'Enter a valid password, password has text only.'])

    def test_register_fail_password_field_has_number(self):

        data = {
            'email': faker.email(),
            'password': faker.random_number(10),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, [
                        'Enter a valid password, password has number only.'])

    def test_register_fail_password_field_has_number_and_character(self):

        data = {
            'email': faker.email(),
            'password': '1234kdhjdhud',
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, [
                        'Enter a valid password, password has number and char only.'])
        
    def test_register_fail_password_field_has_special_character(self):

        data = {
            'email': faker.email(),
            'password': '@!#',
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, [
                        'Enter a valid password, password has special char only.'])
        
    def test_register_fail_password_field_has_special_character_and_num(self):

        data = {
            'email': faker.email(),
            'password': '@!#123',
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, [
                        'Enter a valid password, password has special charand number only.'])

    def test_register_fail_password_field_length_is_short(self):

        data = {
            'email': faker.email(),
            'password': faker.password(7),
            'type': 'student',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['password'].errors, ['Enter a valid password.'])

    def test_register_fail_phone_field_is_blank(self):

        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': 'student',
            'phone': ''
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['phone'].errors, ['Enter a valid phone number.'])








    # def test_register_fail_phone_field_has_text(self):

    #     data = {
    #         'email': faker.email(),
    #         'password': faker.password(),
    #         'type': 'student',
    #         'phone': 'rftgfghhijn'
    #     }

    #     form = RegisterForm(data)

    #     self.assertFalse(form.is_valid())
    #     self.assertTrue(form['phone'].errors, ['Enter a valid phone number.'])






    def test_register_fail_phone_number_already_exists(self):

        test_user = UserFactory()
        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': 'student',
            'phone': test_user.phone
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(CustomUser.objects.filter(
            phone=data['phone']).exists())
        self.assertTrue(form['phone'].errors, ['Entered phone number already exists.'])

    def test_register_fail_type_field_is_blank(self):

        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': '',
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['type'].errors, ['Enter a valid user type.'])

    def test_register_fail_type_field_has_text(self):

        data = {
            'email': faker.email(),
            'password': faker.password(),
            'type': faker.text(10),
            'phone': faker.random_number(10)
        }

        form = RegisterForm(data)

        self.assertFalse(form.is_valid())
        self.assertTrue(form['type'].errors, ['Enter a valid user type.'])

















    # def test_register_post_failed(self):

    #     # print(self.email)

    #     register_url = reverse("register")
    #     data = {
    #         'email': faker.text(10),
    #         'password': faker.text(10),
    #         'type': 'student',
    #         'phone': faker.random_number(20)

    #     }
    #     # print(data['email'], '===========')
    #     # print(data)
    #     response = self.client.post(register_url, data)
    #     form = RegisterForm(data)

    #     self.assertTrue(CustomUser.objects.filter(
    #         email=self.email).exists())
    #     self.assertFalse(form.is_valid())
    #     self.assertTrue(form['email'].errors, ['Enter a valid email address.'])
    #     self.assertTrue(form["password"].errors, ["Password must be atleast 8 characters long.",
    #                                               "Password must contain one Upper and lower character.",
    #                                               "Password must contain atleast one digit.",
    #                                               "Password must contain atleast one special char."])
    #     self.assertTrue(form['phone'].errors, ['Ensure this value has at most 12 characters'])
    #     self.assertEqual(response.status_code, 302)


#     def test_logout(self):

#         self.client.login(email=self.email, password=self.password)

#         logout_url = reverse('logout')
#         response = self.client.get(logout_url)

#         self.assertEqual(response.status_code, 302) # 302 is status code for redirect
#         self.assertNotEqual(response.status_code, 404)
