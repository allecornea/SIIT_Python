description = ('Country', ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])

raw_data = [('AL', [':', ':', ':', ':', ':', ':', ':', '84', ':']),
            ('AT', ['75', '79', '81', '81', '82', '85', '89', '89', '90']),
            ('BA', [':', ':', ':', ':', ':', ':', ':', '69', '72']),
            ('BE', ['77', '78', '80', '83', '82', '85', '86', '87', '90']),
            ('BG', ['45', '51', '54', '57', '59', '64', '67', '72', '75']),
            ('CH', [':', ':', ':', '91', ':', ':', '93', ':', '96']),
            ('CY', ['57', '62', '65', '69', '71', '74', '79', '86', '90']),
            ('CZ', ['67', '73', '73', '78', '79', '82', '83', '86', '87']),
            ('DE', ['83', '85', '88', '89', '90', '92', '93', '94', '95']),
            ('DK', ['90', '92', '93', '93', '92', '94', '97', '93', '95']),
            ('EA', ['74', '76', '79', '81', '83', '85', '87', '89', '90']),
            ('EE', ['69', '74', '79', '83', '88', '86', '88', '90', '90']),
            ('EL', ['50', '54', '56', '66', '68', '69', '71', '76', '79']),
            ('ES', ['63', '67', '70', '74', '79', '82', '83', '86', '91']),
            ('FI', ['84', '87', '89', '90', '90', '92', '94', '94', '94']),
            ('FR', ['76', '80', '82', '83', '83', '86', '86', '89', '90']),
            ('HR', ['61', '66', '65', '68', '77', '77', '76', '82', '81']),
            ('HU', ['63', '67', '70', '73', '76', '79', '82', '83', '86']),
            ('IE', ['78', '81', '82', '82', '85', '87', '88', '89', '91']),
            ('IS', ['93', '95', '96', '96', ':', ':', '98', '99', '98']),
            ('IT', ['62', '63', '69', '73', '75', '79', '81', '84', '85']),
            ('LT', ['60', '60', '65', '66', '68', '72', '75', '78', '82']),
            ('LU', ['91', '93', '94', '96', '97', '97', '97', '93', '95']),
            ('LV', ['64', '69', '72', '73', '76', '77', '79', '82', '85']),
            ('ME', [':', '55', ':', ':', ':', ':', '71', '72', '74']),
            ('MK', [':', '58', '65', '68', '69', '75', '74', '79', '82']),
            ('MT', ['75', '77', '78', '80', '81', '81', '85', '84', '86']),
            ('NL', ['94', '94', '95', '96', '96', '97', '98', '98', '98']),
            ('NO', ['92', '93', '94', '93', '97', '97', '97', '96', '98']),
            ('PL', ['67', '70', '72', '75', '76', '80', '82', '84', '87']),
            ('PT', ['58', '61', '62', '65', '70', '74', '77', '79', '81']),
            ('RO', ['47', '54', '58', '61', '68', '72', '76', '81', '84']),
            ('RS', [':', ':', ':', ':', '64', ':', '68', '73', '80']),
            ('SE', ['91', '92', '93', '90', '91', '94', '95', '93', '96']),
            ('SI', ['73', '74', '76', '77', '78', '78', '82', '87', '89']),
            ('SK', ['71', '75', '78', '78', '79', '81', '81', '81', '82']),
            ('TR', [':', '47', '49', '60', '70', '76', '81', '84', '88']),
            ('UK', ['83', '87', '88', '90', '91', '93', '94', '95', '96']),
            ('XK', [':', ':', ':', ':', ':', ':', '89', '93', '93'])]

# For the implementation it is required:

# Function that prepares the dataset:

# This function will take the raw dataset as an argument
# This function will return a dict with the following structure:

'''
{
'Romania': [{'year': '2019','coverage': 84}, 
            {'year': '2018','coverage': 67},
            ...,{'year': '2011','coverage': 72}],
'Germany': [{'year': '2019','coverage': 94}, 
            {'year': '2018','coverage': 87},
            ...,{'year': '2011','coverage': 82}]
}
'''

import pprint

pp = pprint.PrettyPrinter(indent=4)


def create_dataset(data):
    coverage_by_year_and_country_dict = {}
    for country, index in data:
        for year in description[1]:
            i = description[1].index(year)
            if country in coverage_by_year_and_country_dict.keys():
                coverage_by_year_and_country_dict[country].extend([{'year': year, 'coverage': index[i]}])
            if country not in coverage_by_year_and_country_dict.keys():
                coverage_by_year_and_country_dict[country] = [{'year': year, 'coverage': index[i]}]
    return coverage_by_year_and_country_dict


pp.pprint(create_dataset(raw_data))

print('------------------------------------------------')


# Function to retrieve data for each year:

# This function will take the dataset and year as an argument.
# This function will return any type that you choose.

# get_year_data(dataset, "2019")
#  {'2019': [('Romania', 84), ('Germany', 95), ..., ('Latvia', 85)]}


def get_year_data(data, get_year):
    coverage_by_year = {}
    for country, index in data:
        for year in description[1]:
            if year == get_year:
                i = description[1].index(year)
                if year in coverage_by_year.keys():
                    coverage_by_year[year].extend([(country, index[i])])
                if year not in coverage_by_year.keys():
                    coverage_by_year[year] = [(country, index[i])]
    return coverage_by_year


pp.pprint(get_year_data(raw_data, '2016'))

print('------------------------------------------------')


# Function to retrieve data for each country:

# This function will take the dataset and country as an argument.
# This function will return any type that you choose.

# get_country_data(dataset, "Romania")
# {'Romania': [('2019', 84), ('2018', 86), ..., ('2011', 72)]}


def get_country_data(data, get_country):
    coverage_by_country = {}
    for country, index in data:
        if country == get_country:
            for year in description[1]:
                i = description[1].index(year)
                if country in coverage_by_country.keys():
                    coverage_by_country[country].extend([(year, index[i])])
                if country not in coverage_by_country.keys():
                    coverage_by_country[country] = [(year, index[i])]
    return coverage_by_country


pp.pprint(get_country_data(raw_data, 'RO'))

print('------------------------------------------------')


# function to perform average from an iterable(of year data or country data)

# This function will take an iterable as an argument.
# This function will return a float.


def calculate_average(country_code):
    country_data = get_country_data(raw_data, country_code)
    for index in country_data.values():
        n = 0
        sum_of = 0
        for year, value in index:
            n += 1
            sum_of = sum_of + int(value)
            average = sum_of / n
    return round(average, 2)


print(calculate_average('RO'))

print('------------------------------------------------')

'''
Given the following function:

def greet(name):
    return "Greetings {}!".format(name)
    
Create a decorator called uppercase that will uppercase the result:

@uppercase
def greet(name):
    return "Greetings {}!".format(name)
    
print(greet("World"))
>>> "GREETINGS WORLD!"
'''


def uppercase(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet('Alexandra'))

print('------------------------------------------------')

# Create a decorator called safe_addition that will output a message if the operation cannot be performed correctly
# [is unsafe] and return a correct result [check - floating point inaccuracies], otherwise it will return just the
# result


def safe_addition(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if str(result)[::-1].find('.') > 1:
            return 'Please check the input numbers, there is a floating point inaccuracy!'
        else:
            return result
    return wrapper


@safe_addition
def sum_of(first_number, second_number):
    return first_number + second_number


print(sum_of(1.1, 2.2))
print(sum_of(1.1, 1.1))

print('------------------------------------------------')


# Create a decorator called register that will update a list called print_registry with all the
# decorated functions names.


print_registry = []


def register(func):
    print_registry.append(func.__name__)
    return func


@register
def greet(name):
    return "Greetings {}!".format(name)


def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(print_registry)









