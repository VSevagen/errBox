from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def register_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        # Test data. You cxan check out the songs if you want :)
        self.register_song("Mo Capitaine", "Michel Legris")
        self.register_song("Ici kot nu ete", "Cassiya")
        self.register_song("Bal Souki Souki", "Clarel Armel")


class GetAllSongsTest(BaseViewTest):

    def test_get_all_songs(self):
        #Ensure the songs that were added through setup exist when a GET request is made. 

        # hit the API endpoint
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
        # Get the data from db
        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)