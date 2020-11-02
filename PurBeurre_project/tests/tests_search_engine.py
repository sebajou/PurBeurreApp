import pytest
from request_api_app.search_engine import PopDBFromJsonWithCategories
import json
from schema import Schema, And, Use, Optional
from database_handler_app.models import FoodList, Allergen


class TestsPopDBFromJsonWithCategories:

    def setup_method(self):
        # Open the bonbons_json_data
        with open("bonbons.json", "r") as read_file:
            self.json_for_test = json.load(read_file)

        self.schema = Schema([{
            "food_name": And(str),
            "category": And(str),
            "scora_nova_group": And(int),
            "nutri_score_grad": And(str),
            "food_url": And(str),
            "image_src": And(str),
            "allergen_list": And(str),
        }])

        pop = PopDBFromJsonWithCategories()
        self.dictionary_build_with_json = pop.variables_from_foods_json(data_category_json=self.json_for_test, name_category="bonbon")
        self.dictionary_from_json_bonbon = [[{'food_name': 'aux Plantes Citron - Mélisse', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700946961/aux-plantes-citron-melisse-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/094/6961/front_fr.32.400.jpg', 'allergen_list': ''}], [{'food_name': "Happy'Box", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220033838/happy-box-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/3838/front_fr.91.400.jpg', 'allergen_list': ''}], [{'food_name': 'Dragibus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220025208/dragibus-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/002/5208/front_fr.74.400.jpg', 'allergen_list': ''}], [{'food_name': "Mini Cub'BIO", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346311601/mini-cub-bio-krema', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/631/1601/front_fr.31.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons à la menthe', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3014680009175/bonbons-a-la-menthe-la-vosgienne', 'image_src': 'https://static.openfoodfacts.org/images/products/301/468/000/9175/front_fr.78.400.jpg', 'allergen_list': ''}], [{'food_name': 'Tagada', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220044544/tagada-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/301/468/000/9175/front_fr.78.400.jpg', 'allergen_list': ''}], [{'food_name': 'Chamallows', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009512/chamallows-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9512/front_fr.54.400.jpg', 'allergen_list': ''}], [{'food_name': "m&m's Peanut", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/40111445/m-m-s-peanut', 'image_src': 'https://static.openfoodfacts.org/images/products/40111445/front_fr.17.400.jpg', 'allergen_list': 'en:milk,en:peanuts,en:soybeans'}], [{'food_name': 'Dragolo', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220007822/dragolo-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/7822/front_fr.92.400.jpg', 'allergen_list': 'en:gluten,fr:Dextrose'}], [{'food_name': "Tagada, L'originale", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220033371/tagada-l-originale-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/3371/front_fr.16.400.jpg', 'allergen_list': ''}], [{'food_name': 'Haribo croco', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220035214/haribo-croco', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/5214/front_fr.48.400.jpg', 'allergen_list': ''}], [{'food_name': "M&M's Peanut", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/5000159492874/m-m-s-peanut-mars', 'image_src': 'https://static.openfoodfacts.org/images/products/500/015/949/2874/front_fr.7.400.jpg', 'allergen_list': 'en:milk,en:peanuts,en:soybeans'}], [{'food_name': 'Pastilles Vichy', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346306539/pastilles-vichy', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/630/6539/front_fr.22.400.jpg', 'allergen_list': ''}], [{'food_name': 'Dragibus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220030400/dragibus-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/0400/front_fr.77.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Eucalyptus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700626382/bonbons-eucalyptus-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/062/6382/front_fr.45.400.jpg', 'allergen_list': ''}], [{'food_name': 'Fraises Tagada', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220030417/fraises-tagada-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/0417/front_fr.5.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Suisses aux Plantes sans sucres Menthe Pomme', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700901137/bonbons-suisses-aux-plantes-sans-sucres-menthe-pomme-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/090/1137/front_fr.62.400.jpg', 'allergen_list': 'fr:Une consommation excessive peut avoir des effets laxatifs'}], [{'food_name': "Mini Cub' bio", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346311649/mini-cub-bio-krema', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/631/1649/front_fr.12.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola Menthol', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700626405/ricola-menthol', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/062/6405/front_fr.22.400.jpg', 'allergen_list': ''}], [{'food_name': 'Les Schtroumpfs', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009710/les-schtroumpfs-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9710/front_fr.81.400.jpg', 'allergen_list': ''}], [{'food_name': 'Koala', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740033899/koala-lutti', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/003/3899/front_fr.41.400.jpg', 'allergen_list': 'en:milk,en:soybeans'}], [{'food_name': 'Haribo tirlibibi', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009987/haribo-tirlibibi', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9987/front_fr.63.400.jpg', 'allergen_list': 'en:gluten,en:milk'}], [{'food_name': 'Chamallows Choco', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220043158/chamallows-choco-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/004/3158/front_fr.27.400.jpg', 'allergen_list': 'en:milk'}], [{'food_name': 'Tic Tac Menthe', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3017625073309/tic-tac-menthe-ferrero', 'image_src': 'https://static.openfoodfacts.org/images/products/301/762/507/3309/front_fr.58.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700626368/ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/062/6368/front_fr.35.400.jpg', 'allergen_list': ''}], [{'food_name': 'Intense Mint Menthe Extra-Fraiche', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/8000500119358/intense-mint-menthe-extra-fraiche-tic-tac', 'image_src': 'https://static.openfoodfacts.org/images/products/800/050/011/9358/front_fr.44.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Lutti Scoubidou', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740027317/bonbons-lutti-scoubidou', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/002/7317/front_fr.6.400.jpg', 'allergen_list': ''}], [{'food_name': 'Maltesers', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/5000159437943/maltesers-mars', 'image_src': 'https://static.openfoodfacts.org/images/products/500/015/943/7943/front_fr.40.400.jpg', 'allergen_list': 'en:gluten,en:milk,en:soybeans'}], [{'food_name': 'Mentos Fruit', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/87108026/mentos-fruit', 'image_src': 'https://static.openfoodfacts.org/images/products/87108026/front_fr.26.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola Réglisse', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'c', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700612477/ricola-reglisse', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/061/2477/front_fr.3.400.jpg', 'allergen_list': 'en:soybeans'}], [{'food_name': "Happy'life", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220034804/happy-life-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/4804/front_fr.50.400.jpg', 'allergen_list': ''}], [{'food_name': 'Les schtroumpfs P!K', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220035771/les-schtroumpfs-p-k-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/5771/front_fr.51.400.jpg', 'allergen_list': ''}], [{'food_name': 'Fruits de mer ORIGINAL', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/20012274/fruits-de-mer-original-j-d-gross', 'image_src': 'https://static.openfoodfacts.org/images/products/20012274/front_fr.15.400.jpg', 'allergen_list': 'en:soybeans'}], [{'food_name': "L'authentique petit ourson guimauve", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3173289209598/l-authentique-petit-ourson-guimauve-cemoi', 'image_src': 'https://static.openfoodfacts.org/images/products/317/328/920/9598/front_fr.11.400.jpg', 'allergen_list': 'en:milk'}], [{'food_name': 'Carambar Caramel', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346300780/carambar-caramel-carambar-co', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/630/0780/front_fr.36.400.jpg', 'allergen_list': ''}], [{'food_name': 'Tic Tac goûts Citron Vert & Orange', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4008400390529/tic-tac-gouts-citron-vert-orange', 'image_src': 'https://static.openfoodfacts.org/images/products/400/840/039/0529/front_fr.42.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola Cranberry Bonbons suisses aux plantes', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700614914/ricola-cranberry-bonbons-suisses-aux-plantes', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/061/4914/front_fr.53.400.jpg', 'allergen_list': ''}], [{'food_name': 'Frisk - Menthe Forte', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/5412841601240/frisk-menthe-forte', 'image_src': 'https://static.openfoodfacts.org/images/products/541/284/160/1240/front_fr.22.400.jpg', 'allergen_list': ''}], [{'food_name': "Werther's original sans sucre", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4014400907902/werther-s-original-sans-sucre', 'image_src': 'https://static.openfoodfacts.org/images/products/401/440/090/7902/front_fr.30.400.jpg', 'allergen_list': 'en:milk,en:soybeans'}], [{'food_name': 'Cachou', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/30005068/cachou-lajaunie', 'image_src': 'https://static.openfoodfacts.org/images/products/401/440/090/7902/front_fr.30.400.jpg', 'allergen_list': 'en:milk,en:soybeans'}], [{'food_name': 'Mentos menthe', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/87108019/mentos-menthe', 'image_src': 'https://static.openfoodfacts.org/images/products/87108019/front_fr.53.400.jpg', 'allergen_list': ''}], [{'food_name': 'Haribo Star Mint', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220006603/haribo-star-mint', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/6603/front_fr.21.400.jpg', 'allergen_list': ''}], [{'food_name': "Rotella l'original", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009635/rotella-l-original-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9635/front_fr.7.400.jpg', 'allergen_list': 'en:gluten'}], [{'food_name': 'Bonbons Suisses - Menthe des Montagnes', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700626306/bonbons-suisses-menthe-des-montagnes-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/062/6306/front_fr.17.400.jpg', 'allergen_list': ''}], [{'food_name': 'KitKat Ball', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3033710019526/kitkat-ball-nestle', 'image_src': 'https://static.openfoodfacts.org/images/products/303/371/001/9526/front_fr.33.400.jpg', 'allergen_list': 'en:gluten,en:milk,fr:malt de blé'}], [{'food_name': 'Lutti Longfizz', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740030393/lutti-longfizz', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/003/0393/front_fr.54.400.jpg', 'allergen_list': 'en:gluten'}], [{'food_name': 'Bonbons suisses aux plantes sans sucres Cassis', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700922385/bonbons-suisses-aux-plantes-sans-sucres-cassis-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/092/2385/front_fr.10.400.jpg', 'allergen_list': ''}], [{'food_name': 'Orange Menthe sans sucres avec édulcorant provenant de la stévia', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700922361/orange-menthe-sans-sucres-avec-edulcorant-provenant-de-la-stevia-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/092/2361/front_fr.40.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Plantes saveur caramel', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'c', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700922668/bonbons-plantes-saveur-caramel-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/092/2668/front_fr.31.400.jpg', 'allergen_list': 'en:milk'}], [{'food_name': 'Bubblizz original lutti', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740033875/bubblizz-original-lutti', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/003/3875/front_fr.22.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola aux Plantes', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700614044/ricola-aux-plantes', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/061/4044/front_fr.9.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Suisses aux plantes Eucalyptus Sans sucres avec édulcorants', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700601396/bonbons-suisses-aux-plantes-eucalyptus-sans-sucres-avec-edulcorants-ricola', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/060/1396/front_fr.38.400.jpg', 'allergen_list': ''}], [{'food_name': 'Tic Tac Menthe', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/80052043/tic-tac-menthe', 'image_src': 'https://static.openfoodfacts.org/images/products/80052043/front_fr.29.400.jpg', 'allergen_list': ''}], [{'food_name': 'Haribo Orangina Pik', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220035580/haribo-orangina-pik', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/5580/front_fr.33.400.jpg', 'allergen_list': ''}], [{'food_name': 'Arlequin Original', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740017332/arlequin-original-lutti', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/001/7332/front_fr.28.400.jpg', 'allergen_list': ''}], [{'food_name': 'trolli', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4000512015062/trolli', 'image_src': 'https://static.openfoodfacts.org/images/products/400/051/201/5062/front_fr.5.400.jpg', 'allergen_list': ''}], [{'food_name': 'Bonbons Parfum Miel Citron', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/7622210663443/bonbons-parfum-miel-citron-la-vosgienne', 'image_src': 'https://static.openfoodfacts.org/images/products/762/221/066/3443/front_fr.14.400.jpg', 'allergen_list': ''}], [{'food_name': 'Surffizz goûts fruits extra acide lutti', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740033882/surffizz-gouts-fruits-extra-acide-lutti', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/003/3882/front_fr.34.400.jpg', 'allergen_list': ''}], [{'food_name': 'Oasis', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220036358/oasis-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/6358/front_fr.45.400.jpg', 'allergen_list': ''}], [{'food_name': 'Dragolo', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220022696/dragolo-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/002/2696/front_fr.16.400.jpg', 'allergen_list': ''}], [{'food_name': 'Tic Tac', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/8000500166697/tic-tac', 'image_src': 'https://static.openfoodfacts.org/images/products/800/050/016/6697/front_fr.32.400.jpg', 'allergen_list': ''}], [{'food_name': 'MIAMI P!k', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220034774/miami-p-k-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/4774/front_fr.16.400.jpg', 'allergen_list': 'en:gluten'}], [{'food_name': 'Maltesers (maxi pack)', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/5000159437967/maltesers-maxi-pack-mars', 'image_src': 'https://static.openfoodfacts.org/images/products/500/015/943/7967/front_fr.8.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola aux plantes', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700601624/ricola-aux-plantes', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/060/1624/front_fr.3.400.jpg', 'allergen_list': ''}], [{'food_name': 'Tic Tac Intense Mint', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/8000500166758/tic-tac-intense-mint-ferrero', 'image_src': 'https://static.openfoodfacts.org/images/products/800/050/016/6758/front_fr.53.400.jpg', 'allergen_list': ''}], [{'food_name': 'Haribo zanzigliss', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220025956/haribo-zanzigliss', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/002/5956/front_fr.24.400.jpg', 'allergen_list': 'en:gluten,en:milk'}], [{'food_name': 'CARenSAC', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220030424/carensac-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/0424/front_fr.9.400.jpg', 'allergen_list': ''}], [{'food_name': 'The Pik box', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220041734/the-pik-box-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/004/1734/front_fr.11.400.jpg', 'allergen_list': ''}], [{'food_name': 'Ricola menthe douce des glaciers', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'b', 'food_url': 'https://fr.openfoodfacts.org/produit/7610700626887/ricola-menthe-douce-des-glaciers', 'image_src': 'https://static.openfoodfacts.org/images/products/761/070/062/6887/front_fr.18.400.jpg', 'allergen_list': ''}], [{'food_name': 'Polka', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009567/polka-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9567/front_fr.9.400.jpg', 'allergen_list': 'en:gluten,en:milk'}], [{'food_name': 'Skittles Fruits', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/5000159303774/skittles-fruits', 'image_src': 'https://static.openfoodfacts.org/images/products/500/015/930/3774/front_fr.54.400.jpg', 'allergen_list': ''}], [{'food_name': 'Croco Pik', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220033784/croco-pik-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/3784/front_fr.17.400.jpg', 'allergen_list': ''}], [{'food_name': 'Pastille menthol-eucalyptus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/50819249/pastille-menthol-eucalyptus-fisherman-s-friend', 'image_src': 'https://static.openfoodfacts.org/images/products/50819249/front_fr.23.400.jpg', 'allergen_list': ''}], [{'food_name': 'Mini mints', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/57023397/mini-mints', 'image_src': 'https://static.openfoodfacts.org/images/products/50819249/front_fr.23.400.jpg', 'allergen_list': ''}], [{'food_name': 'Haribo Dragibus Soft', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220034941/haribo-dragibus-soft', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/4941/front_fr.29.400.jpg', 'allergen_list': ''}], [{'food_name': "Calendrier de l'Avent", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/8000500237601/calendrier-de-l-avent-kinder', 'image_src': 'https://static.openfoodfacts.org/images/products/800/050/023/7601/front_fr.27.400.jpg', 'allergen_list': 'en:milk,en:nuts,en:soybeans'}], [{'food_name': 'Bestfizz', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3116740029809/bestfizz-lutti', 'image_src': 'https://static.openfoodfacts.org/images/products/311/674/002/9809/front_fr.25.400.jpg', 'allergen_list': 'en:gluten'}], [{'food_name': 'Skittles', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4009900455299/skittles', 'image_src': 'https://static.openfoodfacts.org/images/products/400/990/045/5299/front_fr.46.400.jpg', 'allergen_list': ''}], [{'food_name': 'Sensation Fruit Framboise & Cranberry', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3046920045315/sensation-fruit-framboise-cranberry-lindt', 'image_src': 'https://static.openfoodfacts.org/images/products/304/692/004/5315/front_fr.35.400.jpg', 'allergen_list': 'en:milk,en:soybeans'}], [{'food_name': "L'Ours d'Or", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009802/l-ours-d-or-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9802/front_fr.23.400.jpg', 'allergen_list': ''}], [{'food_name': 'Maoam Stripes', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4001686522424/maoam-stripes-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/400/168/652/2424/front_fr.17.400.jpg', 'allergen_list': ''}], [{'food_name': 'World Mix', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220041468/world-mix-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/004/1468/front_fr.16.400.jpg', 'allergen_list': 'en:gluten'}], [{'food_name': 'Chamallows', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220046159/chamallows-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/004/6159/front_fr.3.400.jpg', 'allergen_list': ''}], [{'food_name': 'bonbon', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4001686580332/maoam', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/004/6159/front_fr.3.400.jpg', 'allergen_list': ''}], [{'food_name': 'Les Schtroumphs', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220030455/les-schtroumphs-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/0455/front_fr.35.400.jpg', 'allergen_list': ''}], [{'food_name': 'Cocobat', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220059531/cocobat-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/005/9531/front_fr.20.400.jpg', 'allergen_list': ''}], [{'food_name': "M&M's", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/5000159386821/m-m-s', 'image_src': 'https://static.openfoodfacts.org/images/products/500/015/938/6821/front_fr.6.400.jpg', 'allergen_list': 'en:milk,en:peanuts,en:soybeans'}], [{'food_name': "Gom's", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346303149/gom-s-la-pie-qui-chante', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/630/3149/front_fr.4.400.jpg', 'allergen_list': ''}], [{'food_name': 'Fraises Tagada Haribo', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009079/fraises-tagada-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9079/front_fr.12.400.jpg', 'allergen_list': ''}], [{'food_name': "L'ours d'or", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220030431/l-ours-d-or-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/003/0431/front_fr.6.400.jpg', 'allergen_list': ''}], [{'food_name': "Régal'ad", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346307055/regal-ad-krema', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/630/7055/front_fr.7.400.jpg', 'allergen_list': ''}], [{'food_name': 'Pastilles menthol-eucalyptus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/5000357103459/pastilles-menthol-eucalyptus-fisherman-s-friend', 'image_src': 'https://static.openfoodfacts.org/images/products/500/035/710/3459/front_fr.31.400.jpg', 'allergen_list': ''}], [{'food_name': 'Fruit Chewy Dragees Rolls 4 x', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/87108712/fruit-chewy-dragees-rolls-4-x-mentos', 'image_src': 'https://static.openfoodfacts.org/images/products/87108712/front_fr.38.400.jpg', 'allergen_list': ''}], [{'food_name': 'La Vosgienne Parfums Framboise Citron Orange', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3538280837254/la-vosgienne-parfums-framboise-citron-orange', 'image_src': 'https://static.openfoodfacts.org/images/products/87108712/front_fr.38.400.jpg', 'allergen_list': ''}], [{'food_name': 'Mao Croqui', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220006658/mao-croqui-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/6658/front_fr.4.400.jpg', 'allergen_list': ''}], [{'food_name': 'Stoptou', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3664346307048/stoptou-la-pie-qui-chante', 'image_src': 'https://static.openfoodfacts.org/images/products/366/434/630/7048/front_fr.4.400.jpg', 'allergen_list': ''}], [{'food_name': "Werther's original", 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'e', 'food_url': 'https://fr.openfoodfacts.org/produit/40144283/werther-s-original', 'image_src': 'https://static.openfoodfacts.org/images/products/40144283/front_fr.46.400.jpg', 'allergen_list': 'en:milk,en:soybeans'}], [{'food_name': 'Mini chupa chups', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/4601798030055/mini-chupa-chups', 'image_src': 'https://static.openfoodfacts.org/images/products/460/179/803/0055/front_fr.3.400.jpg', 'allergen_list': ''}], [{'food_name': 'Dragibus', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009826/dragibus-haribo', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9826/front_fr.21.400.jpg', 'allergen_list': ''}], [{'food_name': 'bonbon', 'category': 'bonbon', 'scora_nova_group': 4, 'nutri_score_grad': 'd', 'food_url': 'https://fr.openfoodfacts.org/produit/3103220009659', 'image_src': 'https://static.openfoodfacts.org/images/products/310/322/000/9826/front_fr.21.400.jpg', 'allergen_list': ''}]]

    def test_variables_from_foods_json(self):
        """Control Extract useful data from json and stock it in variables corespond to schema"""
        dictionary_schema = self.schema
        dictionary_from_json = self.dictionary_build_with_json
        print(dictionary_from_json)
        # Loop on dictionary extract from json to assert schema of for each products
        for products_num_dict in dictionary_from_json:
            assert dictionary_schema.is_valid(products_num_dict)

    @pytest.mark.django_db(transaction=True)
    def tests_pop_db(self):
        """Verify that database is populate with the dictionary from json file."""
        dictionary_from_json = self.dictionary_from_json_bonbon
        # Populate the database with dictionary from json
        pop = PopDBFromJsonWithCategories()
        pop.pop_db(dictionary_from_json=dictionary_from_json)
        # Stoke data from model in dictionary
        dictionary_from_model = FoodList.objects.values()
        # Loop to assert that data from dictionary_from_json are stock in the database
        for product_from_model in dictionary_from_model:
            for product_from_json in dictionary_from_json[0]:
                assert product_from_model["food_name"] == product_from_json["food_name"]
                assert product_from_model["category"] == product_from_json["category"]
                assert product_from_model["scora_nova_group"] == product_from_json["scora_nova_group"]
                assert product_from_model["nutri_score_grad"] == product_from_json["nutri_score_grad"]
                assert product_from_model["food_url"] == product_from_json["food_url"]
                assert product_from_model["image_src"] == product_from_json["image_src"]
                # Verify the many to many relation between FoodList and Allergen
                allergen_from_model = Allergen.objects.filter(foodlist__id=product_from_model["id"]).values()
                for allergen_from_json in product_from_json["allergen_list"].split(","):
                    for allergen_in_product_model in allergen_from_model:
                        assert allergen_in_product_model['allergen_name'] == allergen_from_json
                # Verify that food_list item contain an id
                assert int(product_from_model["id"])

