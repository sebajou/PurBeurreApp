from django.core.management.base import BaseCommand
from request_api_app import search_engine
from database_handler_app.initial_database_fill_up import fill_up_diet, fill_up_allergen


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_up_diet()
        fill_up_allergen()
        search_engine.pop_db_with_categories()
