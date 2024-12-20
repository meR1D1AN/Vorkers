from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Worker
from .serializers import WorkerSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    """
    CRUD для работников
    """

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        operation_description="Получение списка всех работников",
        operation_summary="Список всех работников",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="limit",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Количество работников на странице",
                required=False,
            ),
            openapi.Parameter(
                name="offset",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Смещение для пагинации",
                required=False,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Успешное получение списка всех работников",
                schema=WorkerSerializer(many=True),
            ),
            400: "Ошибка запроса",
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка работников в бригаде",
        operation_summary="Список работников в бригаде",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="team_id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="ID бригады",
                required=True,
            ),
            openapi.Parameter(
                name="limit",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Количество работников на странице",
                required=False,
            ),
            openapi.Parameter(
                name="offset",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Смещение для пагинации",
                required=False,
            ),
        ],
        responses={
            200: openapi.Response(
                description="Успешное получение списка работников в бригаде",
                schema=WorkerSerializer(many=True),
            ),
            400: "Ошибка запроса",
        },
    )
    def team_list(self, request, team_id, *args, **kwargs):
        self.queryset = self.queryset.filter(team_number=team_id)
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Создание работника",
        operation_description="Создание нового работника",
        tags=["Работник"],
        responses={
            201: openapi.Response(
                description="Успешное создание работника",
                schema=WorkerSerializer(),
            ),
            400: "Ошибка запроса",
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Получение детальной информации о работнике",
        operation_description="Возвращает полную информацию о конкретном работнике по его идентификатору",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор работника",
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Успешное получение информации о работнике",
                schema=WorkerSerializer(),
            ),
            404: "Работник не найден",
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Обновление информации о работнике",
        operation_description="Обновляет полную информацию о конкретном работнике по его идентификатору",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор работника",
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Успешное обновление информации о работнике",
                schema=WorkerSerializer(),
            ),
            404: "Работник не найден",
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Частичное обновление информации о работнике",
        operation_description="Обновляет частичную информацию о конкретном работнике по его идентификатору",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор работника",
                required=True,
            )
        ],
        responses={
            200: openapi.Response(
                description="Успешное обновление информации о работнике",
                schema=WorkerSerializer(),
            ),
            404: "Работник не найден",
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Удаление работника",
        operation_description="Удаляет работника по его идентификатору",
        tags=["Работник"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор работника",
                required=True,
            )
        ],
        responses={
            204: "Работник успешно удален",
            404: "Работник не найден",
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
