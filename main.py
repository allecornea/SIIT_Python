def shop_list():
    colours = ['green', 'blue', 'white', 'black', 'pink', 'gray', 'yellow', 'red', 'orange', 'purple', 'lila']
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    categories = ['blouse', 'shirt', 'trousers', 'scarf', 'skirt', 'dress', 'bag']

    # Hobby Shop
    # Requirements:
    # - Have at least 400 articles in the shop
    # - Have at least four types of articles (shirt, scarf, glove, heat)
    # - Have at least five sizes (S M L XL XXL) for each type of article
    # - To be able to sell the latest article that was added to the shop
    # - To be able to sell any item that is in the shop
    # - To restock the shop with new items

    shop_articles = [(x, y, z) for x in categories
                     for y in sizes for z in colours]
    print(shop_articles)
    print(len(shop_articles))
    print(shop_articles[len(shop_articles) - 1])

    # Remove the last article in the shop

    shop_articles.pop(len(shop_articles) - 1)
    print(len(shop_articles))
    print(shop_articles[len(shop_articles) - 1])

    # Add a new item to the shop

    add_item(shop_articles, 'blouse', 'M', 'lila')
    print(len(shop_articles))
    print(shop_articles[len(shop_articles) - 1])

    # Remove item from the shop

    item_to_be_removed = ('shirt', 'XL', 'black')
    remove_item(shop_articles, item_to_be_removed)
    print(len(shop_articles))

    # Check if item was removed

    if item_to_be_removed not in shop_articles:
        print(f'Item {item_to_be_removed} was removed from the shop')
    else:
        print(f'Item {item_to_be_removed} is still available!')


def add_item(shop_articles, category, size, colour):
    shop_articles.append((category, size, colour))


def remove_item(shop_articles, item):
    shop_articles.remove(item)


if __name__ == '__main__':
    shop_list()
