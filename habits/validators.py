from rest_framework.exceptions import ValidationError


def time_of_complete_limit(value):
    if value <= 0:
        raise ValidationError('Время выполнения привычки не может быть отрицательным или равным нулю')
    if value > 120:
        raise ValidationError('Время выполнения привычки не может быть больше 120 секунд')


def frequency_limit(value):
    if value <= 0:
        raise ValidationError('Частота выполнения привычки не может быть отрицательной или равной нулю')
    if value > 7:
        raise ValidationError('Чтобы выработать привычку необходимо совершать ее не реже чем 1 раз в 7 дней')


class AssociatedHabitCompletedValidator:
    # Атрибут доступа к полям сериализатора
    requires_context = True

    @staticmethod
    def check_sign_of_pleasant(serializer_field):
        """Если поле sign_of_pleasant = True, то поле associated_habit не может быть пустыми"""
        if (serializer_field.data.get("sign_of_pleasant") is True
                and
                serializer_field.data.get('associated_habit') is None):

            raise ValidationError('Укажите вознаграждение')
        if (serializer_field.data.get("sign_of_pleasant") is False
                and
                serializer_field.data.get('associated_habit') is not None):

            raise ValidationError('Укажите признак наличия вознаграждения')
