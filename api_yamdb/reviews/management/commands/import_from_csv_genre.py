import csv
from django.core.management.base import BaseCommand
from reviews.models import Genre

FILE_PATH = 'static/data/genre.csv'
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
                if Genre.objects.filter(id=row['id']).exists():
                    Genre.objects.filter(id=row['id']).delete()
                    print(
                        f'Строка с id {row_id} существует '
                        f'и будет перезаписана'
                    )
                genre = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                genre.save()
        print(f'Импоорт {FILE_NAME} завершен.')

# id,name,slug
