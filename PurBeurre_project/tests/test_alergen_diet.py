import pytest
from request_api_app.alergen_diet import IsFood
import json


class TestIsFood:

    def setup_method(self):
        self.allergen_list = ['en:fish', 'en:eggs']
        self.diet_type = 'en:vegan'
        self.id_food = 555
        self.id_food_two = 612
        with open("dict_healthy_substitute_before_allergen_filter.json", "r") as read_file:
            self.food_list_with_allergen = json.load(read_file)
        with open("dict_healthy_substitute_before_diet_filter.json", "r") as read_file:
            self.food_list_with_diet = json.load(read_file)
        with open("dict_healthy_substitute_after_allergen_filter.json", "r") as read_file:
            self.food_list_without_allergen = json.load(read_file)
        with open("dict_healthy_substitute_after_diet_filter.json", "r") as read_file:
            self.food_list_without_diet = json.load(read_file)
        with open("food_list_with_unconvenient_diet.json", "r") as read_file:
            self.food_list_with_unconvenient_diet = json.load(read_file)
        self.id_user = 1
        self.id_user2 = 11

    """@pytest.mark.avoid
    @pytest.mark.django_db(transaction=True)
    def test_is_allergen(self):
        allergens = self.allergen_list
        a_food = self.id_food
        is_or_not = IsFood()

        bool_is_allergen = is_or_not.is_allergen(allergen_list=allergens, id_food=a_food)

        assert bool_is_allergen

    @pytest.mark.avoid
    @pytest.mark.django_db(transaction=True)
    def test_is_diet(self):
        a_food2 = self.id_food_two
        a_diet = self.diet_type
        is_or_not2 = IsFood()

        bool_is_diet = is_or_not2.is_diet(diet_type=a_diet, id_food=a_food2)

        assert not bool_is_diet"""

    @pytest.mark.django_db(transaction=True)
    def test_remove_food_from_diet(self):
        with_diet = self.food_list_with_diet
        without_diet = self.food_list_without_diet
        unconvenient_diet = self.food_list_with_unconvenient_diet
        # diet_of_user = create_user_diet()
        user = self.id_user2
        remove_from_list2 = IsFood()

        calc_list_without_diet = remove_from_list2.remove_food_from_diet(food_dict=with_diet, user_id=user)

        for element in unconvenient_diet:
            assert element not in calc_list_without_diet

    @pytest.mark.django_db(transaction=True)
    def test_remove_food_from_allergen(self):
        with_allergen = self.food_list_with_allergen
        without_allergen = self.food_list_without_allergen
        user = self.id_user
        remove_from_list = IsFood()

        calc_list_without_allergen = remove_from_list.remove_food_from_allergen(food_dict=with_allergen, user_id=user)

        for element in without_allergen:
            assert element in calc_list_without_allergen
