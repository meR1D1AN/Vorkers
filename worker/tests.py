from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Worker, SpecializationChoices


class WorkerAPITests(APITestCase):
    def setUp(self):
        self.worker = Worker.objects.create(
            last_name="Иванов",
            team_number=1,
            salary=10000,
            specialization=SpecializationChoices.CHERNOVA_OTDELKA,
        )

    def test_create_worker(self):
        """ Тест создания работников """
        url = reverse('worker:worker-list')  # Убедитесь, что это правильное имя URL
        data = {
            "last_name": "Новиков",
            "team_number": 1,
            "salary": 15000,
            "specialization": SpecializationChoices.CHERNOVA_OTDELKA,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Worker.objects.count(), 2)  # Проверяем, что работник добавлен


    def test_list_workers(self):
        url = reverse('worker:worker-list')  # Убедитесь, что это правильное имя URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_worker(self):
        url = reverse('worker:worker-detail', args=[self.worker.id])  # Убедитесь, что это правильное имя URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], self.worker.last_name)

    def test_update_worker(self):
        url = reverse('worker:worker-detail', args=[self.worker.id])  # Убедитесь, что это правильное имя URL
        data = {
            "last_name": "Героев",
            "team_number": 1,
            "salary": 11000,
            "specialization": SpecializationChoices.CHERNOVA_OTDELKA,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.last_name, "Героев")

    def test_partial_update_worker(self):
        url = reverse('worker:worker-detail', args=[self.worker.id])  # Убедитесь, что это правильное имя URL
        data = {
            "salary": 12000,
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.worker.refresh_from_db()
        self.assertEqual(self.worker.salary, 12000)

    def test_delete_worker(self):
        url = reverse('worker:worker-detail', args=[self.worker.id])  # Убедитесь, что это правильное имя URL
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Worker.objects.count(), 0)  # Проверяем, что работник удален
