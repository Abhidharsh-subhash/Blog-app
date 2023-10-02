from rest_framework.test import APITestCase,APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .views import listcreatepost
from django.contrib.auth import get_user_model
import json
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken


User=get_user_model()

class HelloWorldTestCase(APITestCase):

    def test_hello_world(self):
        response=self.client.get(reverse('homepage'))
        # self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['message'],'Hello world, GET')

class PostListCreateTestCase(APITestCase):
    #while using factory we have to manually associate a user with the specific post
    # def setUp(self):
    #     self.factory=APIRequestFactory()
    #     self.view=listcreatepost.as_view()
    #     self.url=reverse('listcreatepost')
    #     self.user=User.objects.create(
    #         username='jonathan',
    #         email='jonathan@gmail.com',
    #         password='jonathan@123'
    #     )

    # def test_list_posts(self):
    #     request=self.factory.get(self.url)
    #     response=self.view(request)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)

    #this test case is for creating post with by providing access token for it
    # def test_post_creation(self):
    #     sample_post={
    #         'title':'sample title',
    #         'content':'sample content'
    #     }
    #     # Create a refresh token for the user
    #     refresh = RefreshToken.for_user(self.user)
    #     # Obtain the access token from the refresh token
    #     access_token = AccessToken.for_user(self.user)
    #     token = str(access_token)

    #     # Include the token in the request headers for authentication
    #     headers = {
    #         'HTTP_AUTHORIZATION': f'Bearer {token}'
    #     }
    #     request=self.factory.post(self.url, json.dumps(sample_post), content_type='application/json', **headers)
    #     request.user=self.user
    #     response=self.view(request)
    #     self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def setUp(self):
        self.url=reverse('listcreatepost')

    #method that allow us to authenticate a user
    def authenticate(self):
        self.client.post(reverse('SignUpView'),{
            'email':'johanathan@gmail.com',
            'username':'jonathan',
            'password':'jonathan@123'
        })
        response=self.client.post(reverse('LoginView'),{
            'email':'johanathan@gmail.com',
            'password':'jonathan@123'
        })
        token=response.data['token']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_list_posts(self):
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_post_creation(self):
        self.authenticate()
        sample_data={
            'title':'sample title',
            'content':'sample content'
        }
        response=self.client.post(self.url,sample_data)
        # self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'],sample_data['title'])

    
    
