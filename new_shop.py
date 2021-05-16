from random import randint


def new_shop_list():
    colours = ['green', 'blue', 'white', 'black', 'yellow', 'red', 'orange']
    sizes = ['S', 'M', 'L', 'XL', 'XXL']
    categories = ['blouse', 'shirt', 'trousers', 'skirt', 'dress']

    import random

    shop_articles = []

    for category in categories:
        for size in sizes:
            for colour in colours:
                for quantity in [randint(2, 6)]:
                    shop_articles.append((category, size, colour, quantity))

    print(shop_articles)

    # Check total number of items in the shop

    total_items = sum(quantity[3] for quantity in shop_articles)
    print(total_items)

    category = random.choice(categories)
    size = random.choice(sizes)
    colour = random.choice(colours)
    added_quantity = randint(5, 11)

    add_item(shop_articles, category, size, colour, added_quantity)

    print(f'{added_quantity} {colour} {category}s of size {size} have been added to the shop')

    total_items = sum(quantity[3] for quantity in shop_articles)
    print(total_items)

    # Remove item

    category = random.choice(categories)
    size = random.choice(sizes)
    colour = random.choice(colours)
    removed_quantity = randint(5, 11)
    print(removed_quantity)

    remove_item(shop_articles, category, size, colour, removed_quantity)


def remove_item(shop_articles, category, size, colour, removed_quantity):
    if removed_quantity < shop_articles((category, size, colour)[3]):
        print(f'{removed_quantity} is not available. Please select less')
    shop_articles.remove(category, size, colour, removed_quantity)


def add_item(shop_articles, category, size, colour, added_quantity):
    shop_articles.append((category, size, colour, added_quantity))


if __name__ == '__main__':
    new_shop_list()
