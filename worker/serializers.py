from rest_framework import serializers
from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

    def validate_salary(self, value):
        if value < 0:
            raise serializers.ValidationError("Зарплата не может быть отрицательной")
        return value
