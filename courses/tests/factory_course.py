import factory
from courses.models import Course
from faker import Factory
from users.tests.factory_user import UserFactory

faker = Factory.create()


class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course
        
    instructor = factory.SubFactory(UserFactory)
    name = faker.text(10)
    image = str(faker.text(10)),
    duration = '3 months'
    fees = faker.random_number(5)
    type = 'online'
    description = faker.text(15)

    # @classmethod
    # def _create(cls, model_class, *args, **kwargs):
    #     password = kwargs.pop("password", None)
    #     obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)
    #     # ensure the raw password gets set after the initial save
    #     obj.set_password(password)
    #     obj.save()
    #     return obj
