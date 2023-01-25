import csv
from django.core.management.base import BaseCommand
from reviews.models import Title, Categories

FILE_PATH = 'static/data/titles.csv'
FILE_NAME = FILE_PATH.split('/')[2]


class Command(BaseCommand):
    help = f'Импорт данных {FILE_PATH}'

    def handle(self, *args, **kwargs):

        print(f'Импорт из {FILE_PATH}:')

        with open(f'{FILE_PATH}', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            next(reader)

            for row in reader:
                row_id = row['id']
                row_name = row['name']
                print(row)
                if Title.objects.filter(id=row['id']).exists():
                    Title.objects.filter(id=row['id']).delete()
                    print(
                        f'Строка с id {row_id} существует '
                        f'и будет перезаписана'
                    )
                if Title.objects.filter(name=row['name']).exists():
                    print(
                        f'Строка с name {row_name} существует. '
                        f'name будет модифицировано'
                    )
                    title = Title(
                        id=row['id'],
                        name=row['name'] + '*',
                        year=row['year'],
                        category=Categories(pk=row['category'])
                    )
                    title.save()
                    continue
                title = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Categories(pk=row['category'])
                )
                title.save()
        print(f'Импоорт {FILE_NAME} завершен.')

# id,name,year,category
