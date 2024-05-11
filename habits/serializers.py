from rest_framework import serializers

from habits.models import Habits
from habits.validators import time_of_complete_limit, frequency_limit
from habits.validators import AssociatedHabitCompletedValidator


class HabitsSerializer(serializers.ModelSerializer):
    time_of_complete = serializers.IntegerField(validators=[time_of_complete_limit])
    frequency = serializers.IntegerField(validators=[frequency_limit])

    associated_habit = serializers.CharField(validators=[AssociatedHabitCompletedValidator.check_sign_of_pleasant],
                                             allow_null=True, required=False)

    class Meta:
        model = Habits
        fields = ("id", "owner", "place", "time", "action", "sign_of_pleasant", "associated_habit", "frequency",
                  "time_of_complete", "is_public")
