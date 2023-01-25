import csv
from django.core.management.base import BaseCommand
from reviews.models import Comment, User

FILE_PATH = 'static/data/comments.csv'
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
                if Comment.objects.filter(id=row['id']).exists():
                    Comment.objects.filter(id=row['id']).delete()
                    print(
                        f'Строка с id {row_id} существует '
                        f'и будет перезаписана'
                    )
                category = Comment(
                    id=row['id'],
                    review_id=row['review_id'],
                    text=row['text'],
                    author=User.objects.get(pk=row['author']),
                    pub_date=row['pub_date'],
                )
                category.save()
        print(f'Импоорт {FILE_NAME} завершен.')

# id,review_id,text,author,pub_date
