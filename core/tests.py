from django.test import TestCase
from .models import Thing

class ThingModelTest(TestCase):
    def test_create_thing(self):
        thing = Thing.objects.create(name="Test Thing")
        self.assertEqual(Thing.objects.count(), 1)
        self.assertEqual(thing.name, "Test Thing")

class HelloWorldViewTest(TestCase):
    def test_hello_world_view_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world!")
