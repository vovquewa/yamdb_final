import csv

from django.core.management.base import BaseCommand
from reviews.models import Review, Title, User

FILE_PATH = 'static/data/review.csv'
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
                if Review.objects.filter(id=row['id']).exists():
                    Review.objects.filter(id=row['id']).delete()
                    print(
                        f'Строка с id {row_id} существует '
                        f'и будет перезаписана'
                    )
                if not Title.objects.filter(id=row['title_id']).exists():
                    row_title = row['title_id']
                    print(
                        f'Тайтла с id {row_title} не существует '
                        f'строка будет игнорирована'
                    )
                    continue
                review = Review(
                    id=row['id'],
                    title_id=row['title_id'],
                    text=row['text'],
                    author=User(pk=row['author']),
                    score=row['score'],
                    pub_date=row['pub_date'],
                )
                review.save()
        print(f'Импоорт {FILE_NAME} завершен.')

# id,title_id,text,author,score,pub_date
