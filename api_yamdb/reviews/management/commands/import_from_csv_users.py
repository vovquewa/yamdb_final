import csv

from django.core.management.base import BaseCommand
from reviews.models import User

FILE_PATH = 'static/data/users.csv'
FILE_NAME = FILE_PATH.split('/')[2]


class Command(BaseCommand):
    help = f'Импорт данных {FILE_PATH}'

    def handle(self, *args, **kwargs):

        print(f'Импорт из {FILE_PATH}:')

        with open(f'{FILE_PATH}', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                row_id = row['id']
                print(row)
                if User.objects.filter(id=row['id']).exists():
                    User.objects.filter(id=row['id']).delete()
                    print(
                        f'Строка с id {row_id} существует '
                        f'и будет перезаписана'
                    )
                category = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                )
                category.save()
        print(f'Импоорт {FILE_NAME} завершен.')

# id,username,email,role,bio,first_name,last_name
