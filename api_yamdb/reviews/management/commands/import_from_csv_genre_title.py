import csv

from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Genre, Title

FILE_PATH = '.genre_title.csv'
FILE_NAME = FILE_PATH.split('/')[2]


class Command(BaseCommand):
    help = f'Импорт данных {FILE_PATH}'

    def handle(self, *args, **kwargs):
        with open(f'{FILE_PATH}', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                print(row)
                title = get_object_or_404(Title, id=row['title_id'])
                genre = get_object_or_404(Genre, id=row['genre_id'])

                title.save()
                title.genre.add(genre)

# id,title_id,genre_id
