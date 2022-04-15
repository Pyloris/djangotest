from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

	def setUp(self):
		Post.objects.create(text="hello world")

	def test_text(self):
		post=Post.objects.get(id=1)
		expected_object_name = f'{post.text}'
		self.assertEqual(expected_object_name, 'hello world')


class HomePage(TestCase):
	# check for homepage
	def test_homepage(self):
		resp = self.client.get("/")
		self.assertEqual(resp.status_code, 200)

	# check if home points to home
	def test_if_home(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	# test if correct template was used
	def test_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'base.html')