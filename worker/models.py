from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.db import models


class SpecializationChoices(models.TextChoices):
    """
    Класс специализаций
    """

    PRORAB = "Прораб", "Прораб"
    BRIGADIR = "Бригадир", "Бригадир"
    CHISTOVAYA_OTDELKA = "Чистовая отделка", "Чистовая отделка"
    CHERNOVA_OTDELKA = "Черновая отделка", "Черновая отделка"


class Worker(models.Model):
    """
    Класс работников бригады
    """

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите фамилию",
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s-]+$',
                message="Фамилия должна содержать только русские буквы"
            )
        ]
    )
    team_number = models.IntegerField(
        verbose_name="Номер бригады",
        help_text="Введите номер бригады",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(2),
        ],
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Зарплата",
        help_text="Введите зарплату",
    )
    specialization = models.CharField(
        choices=SpecializationChoices.choices,
        default=SpecializationChoices.CHERNOVA_OTDELKA,
        max_length=50,
        verbose_name="Специализация",
        help_text="Выберите специализацию",
    )

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        ordering = ["last_name"]

    def __str__(self):
        return f"{self.last_name} - {self.specialization}"
