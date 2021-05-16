# Hobby Shop
# Requirements:
# - Have at least 400 articles in the shop - DONE
# - Have at least four types of articles (shirt, scarf, glove, heat) - DONE
# - Have at least five sizes (S M L XL XXL) for each type of article - DONE
# - To be able to sell the latest article that was added to the shop - DONE
# - To be able to sell any item that is in the shop - DONE
# - To restock the shop with new items - DONE

import random
from random import randint

# Define lists for the product categories, sizes, and colours

colours = ['green', 'blue', 'white', 'black', 'yellow', 'red', 'orange']
sizes = ['S', 'M', 'L', 'XL', 'XXL']
categories = ['blouses', 'shirts', 'trousers', 'skirts', 'dresses']

# Generate items in the shop, each article represents a list with the following elements:
# category, size, colour and random quantity

shop_articles = []

for category in categories:
    for size in sizes:
        for colour in colours:
            for quantity in [random.randint(3, 5)]:
                shop_articles.append([category, size, colour, quantity])

# Check total number of items in the shop to ensure there are more than 400 articles (non-distinct) in the shop

total_items = sum(article[3] for article in shop_articles)
print(f'There are currently {total_items} items in the shop.')

print('___________________________________________________\n'
      'Let\'s start by adding a random article to the shop:\n'
      '___________________________________________________')

def add_item():

    # Random selection of the item to be increased

    item_category = random.choice(categories)
    item_size = random.choice(sizes)
    item_colour = random.choice(colours)
    added_quantity = random.randint(3, 5)

    item_increased = [item for item in shop_articles if item_category in item if item_size in item if
                      item_colour in item]

    for item in shop_articles:
        if item == item_increased[0]:
            print(f'There are currently {item[3]} {item_colour} {item_category} of size {item_size} in the shop.')
            item[3] = item[3] + added_quantity
            print(f'+++ Another {added_quantity} have been added. There are now {item[3]} {item_colour} {item_category} '
                  f'of size {item_size} in the shop.')

    # Recheck total number of items in the shop to ensure new items have been added

    total_items = sum(quantity[3] for quantity in shop_articles)

    print(f'+++ Since {added_quantity} {item_colour} {item_category} of size {item_size} have been added, '
          f'there are now {total_items} items in the shop.')

    print('__________________________________________________________\n'
          'Now let\'s remove the last item that was added to the shop:\n'
          '__________________________________________________________')

def remove_last_item():

    removed_category = shop_articles[len(shop_articles) - 1][0]
    removed_size = shop_articles[len(shop_articles) - 1][1]
    removed_colour = shop_articles[len(shop_articles) - 1][2]
    removed_quantity = shop_articles[len(shop_articles) - 1][3]

    shop_articles.pop(len(shop_articles) - 1)

    removed_total_items = sum(quantity[3] for quantity in shop_articles)

    print(f'--- {removed_quantity} {removed_colour} {removed_category} of size {removed_size} have been removed '
          f'from the shop.\n'
          f'--- There are now {removed_total_items} items in the shop.')

    print('__________________________________\n'
          'Now let\'s remove a random article:\n'
          '__________________________________')

def remove_item():

    # Random selection of item to be decreased

    removed_item_category = random.choice(categories)
    removed_item_size = random.choice(sizes)
    removed_item_colour = random.choice(colours)
    removed_quantity = randint(4, 6)
    available_quantity = shop_articles[len(shop_articles) - 1][3]

    item_decreased = [item for item in shop_articles if removed_item_category in item if removed_item_size in item
                      if removed_item_colour in item]

    for item in shop_articles:
        if item == item_decreased[0]:
            if removed_quantity <= item[3]:
                print(f'There are currently {item[3]} {removed_item_colour} {removed_item_category} of size '
                      f'{removed_item_size} in the shop.')
                item[3] = item[3] - removed_quantity
                new_total_items = sum(quantity[3] for quantity in shop_articles)
                print(f'--- {removed_quantity} {removed_item_colour} {removed_item_category} of size {removed_item_size} '
                      f'have been removed from the shop, leaving {item[3]} in stock.\n'
                      f'--- There are now {new_total_items} items in the shop.')
            else:
                print(f'!!! The requested quantity ({removed_quantity}) is not available for item: '
                      f'{removed_item_category}, {removed_item_size}, {removed_item_colour}. '
                      f'The available quantity is {available_quantity}.')


if __name__ == '__main__':
    add_item()
    remove_last_item()
    remove_item()
