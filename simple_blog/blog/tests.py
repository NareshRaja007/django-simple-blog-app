from django.test import TestCase
from django.urls import reverse
from .models import BlogPost

class BlogPostModelTest(TestCase):

    def test_create_blog_post(self):
        """Test creating a blog post successfully"""
        post = BlogPost.objects.create(title="Test Post", content="This is a test blog post.")
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "This is a test blog post.")

class BlogPostViewsTest(TestCase):

    def setUp(self):
        """Set up a sample blog post for testing"""
        self.post = BlogPost.objects.create(title="Sample Post", content="Sample content")

    def test_list_blog_posts(self):
        """Test if the list view displays posts correctly"""
        response = self.client.get(reverse('list_blog_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Post")

    def test_create_blog_post(self):
        """Test creating a blog post through the form"""
        response = self.client.post(reverse('create_blog_post'), {
            'title': 'New Post',
            'content': 'This is a new blog post.'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(BlogPost.objects.count(), 2)  
