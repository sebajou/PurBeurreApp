from django.core.management.base import BaseCommand
from request_api_app import search_engine


class Command(BaseCommand):
    def handle(self, *args, **options):
        search_engine.pop_db_with_categories()
