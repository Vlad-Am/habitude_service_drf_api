from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@test.ru",
            is_staff=True,
            is_active=True,
            is_superuser=False
        )
        self.user.set_password('test_user')
        self.user.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            place='test_place',
            action='test_action',
            owner=self.user
        )

    def test_create_habit(self):
        """Тестирование создания привычек"""

        data = {
            'place': 'test_create',
            'action': 'test_create',
            'owner': self.user.pk,
            "time_of_complete": 100,
            "frequency": 2
        }

        response = self.client.post('/habits/habits/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)

    def test_list_habit(self):
        """Тестирование вывода списка привычек"""

        response = self.client.get('/habits/habits/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'owner': self.user.pk,
                            'place': 'test_place',
                            'time': self.habit.time,
                            'data': self.habit.data.strftime('%Y-%m-%d'),
                            'action': 'test_action',
                            'sign_of_pleasant': self.habit.sign_of_pleasant,
                            'associated_habit': self.habit.associated_habit,
                            'frequency': self.habit.frequency,
                            'time_of_complete': self.habit.time_of_complete,
                            'is_public': self.habit.is_public

                        }
                    ]
            }
        )

    def test_update_habit(self):
        """Тестирование изменения привычки"""

        change_data = {
            'place': 'place_update',
            'action': 'action_update'
        }
        response = self.client.patch(f'/habits/habits/{self.habit.id}/', data=change_data)
        self.maxDiff = None

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'owner': self.user.pk,
                'place': 'place_update',
                'time': self.habit.time,
                'data': self.habit.data.strftime('%Y-%m-%d'),
                'action': 'action_update',
                'sign_of_pleasant': self.habit.sign_of_pleasant,
                'associated_habit': self.habit.associated_habit,
                'frequency': self.habit.frequency,
                'time_of_complete': self.habit.time_of_complete,
                'is_public': self.habit.is_public
            }
        )

    def test_duration_habit(self):
        """Тестирование создания привычки со временем исполнения более 2 минут"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'time_of_complete': '130',
            'owner': self.user.pk,
        }
        response = self.client.post('/habits/habits/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_periodicity_habit(self):
        """Тестирование создания привычки с периодичностью менее одного раза в неделю"""

        data = {
            'place': 'test_place',
            'action': 'test_action',
            'frequency': 8,
            'owner': self.user.pk
        }
        response = self.client.post('/habits/habits/', data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
