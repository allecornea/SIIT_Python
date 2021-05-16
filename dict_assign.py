# Using data from Eurostat, create a list of tuples representing the “Self-perceived health by country and sex,
# age group >16, for people living in cities” for 2017-2018. Have at least 30 values in your dataset.
# - The dataset will have the following structure: > [ > (country, year, sex, health_index) > ]
# Example: > [(‘France’, 2017, M, 12), …]

dataset = [('Belgium', 'F', '2017', 22.2),
           ('Bulgaria', 'F', '2017', 0),
           ('Czechia', 'F', '2017', 13.6),
           ('Denmark', 'F', '2017', 35.6),
           ('Germany', 'F', '2017', 15.9),
           ('Greece', 'F', '2017', 43.2),
           ('Spain', 'F', '2017', 25.5),
           ('France', 'F', '2017', 16.6),
           ('Italy', 'F', '2017', 13.4),
           ('Hungary', 'F', '2017', 5.9),
           ('Netherlands', 'F', '2017', 22.5),
           ('Poland', 'F', '2017', 0),
           ('Portugal', 'F', '2017', 19.1),
           ('Romania', 'F', '2017', 0),
           ('Slovenia', 'F', '2017', 15.4),
           ('Sweden', 'F', '2017', 24.8),
           ('Finland', 'F', '2017', 26.3),
           ('Norway', 'F', '2017', 36.3),
           ('Switzerland', 'F', '2017', 28.9),
           ('United Kingdom', 'F', '2017', 39),
           ('Belgium', 'M', '2017', 26.8),
           ('Bulgaria', 'M', '2017', 0),
           ('Czechia', 'M', '2017', 23.9),
           ('Denmark', 'M', '2017', 17.2),
           ('Germany', 'M', '2017', 16.2),
           ('Greece', 'M', '2017', 55.6),
           ('Spain', 'M', '2017', 17.5),
           ('France', 'M', '2017', 16.5),
           ('Italy', 'M', '2017', 15.8),
           ('Hungary', 'M', '2017', 21.2),
           ('Netherlands', 'M', '2017', 27.4),
           ('Poland', 'M', '2017', 29.5),
           ('Portugal', 'M', '2017', 16.3),
           ('Romania', 'M', '2017', 0),
           ('Slovenia', 'M', '2017', 15.7),
           ('Sweden', 'M', '2017', 34.3),
           ('Finland', 'M', '2017', 22),
           ('Norway', 'M', '2017', 36.2),
           ('Switzerland', 'M', '2017', 33.6),
           ('United Kingdom', 'M', '2017', 42),
           ('Belgium', 'F', '2018', 22.5),
           ('Bulgaria', 'F', '2018', 0),
           ('Czechia', 'F', '2018', 17.8),
           ('Denmark', 'F', '2018', 27.5),
           ('Germany', 'F', '2018', 17.1),
           ('Greece', 'F', '2018', 53.1),
           ('Spain', 'F', '2018', 24.9),
           ('France', 'F', '2018', 17.8),
           ('Italy', 'F', '2018', 18.9),
           ('Hungary', 'F', '2018', 4.8),
           ('Netherlands', 'F', '2018', 23.8),
           ('Poland', 'F', '2018', 16.5),
           ('Portugal', 'F', '2018', 16.8),
           ('Romania', 'F', '2018', 0),
           ('Slovenia', 'F', '2018', 16.3),
           ('Sweden', 'F', '2018', 16.8),
           ('Finland', 'F', '2018', 21.1),
           ('Norway', 'F', '2018', 25.3),
           ('Switzerland', 'F', '2018', 29.8),
           ('United Kingdom', 'F', '2018', 36.8),
           ('Belgium', 'M', '2018', 25.4),
           ('Bulgaria', 'M', '2018', 0),
           ('Czechia', 'M', '2018', 24.6),
           ('Denmark', 'M', '2018', 33.5),
           ('Germany', 'M', '2018', 16.1),
           ('Greece', 'M', '2018', 56.7),
           ('Spain', 'M', '2018', 34.9),
           ('France', 'M', '2018', 18.5),
           ('Italy', 'M', '2018', 21.5),
           ('Hungary', 'M', '2018', 10),
           ('Netherlands', 'M', '2018', 28.5),
           ('Poland', 'M', '2018', 16),
           ('Portugal', 'M', '2018', 14),
           ('Romania', 'M', '2018', 0),
           ('Slovenia', 'M', '2018', 15.6),
           ('Sweden', 'M', '2018', 32.7),
           ('Finland', 'M', '2018', 23.3),
           ('Norway', 'M', '2018', 20.8),
           ('Switzerland', 'M', '2018', 32.1),
           ('United Kingdom', 'M', '2018', 41.4)]

# Using only comprehensions, create the following dicts:
# - two dicts that group all data by country for each year >
# health_index_2017 = {‘France’: [sex, health_index]} > health_index_2017 = {‘France’: [sex, health_index]}

health_index_2017 = {}
health_index_2018 = {}

for country, sex, year, h_index in dataset:
    if year == '2017':
        if country not in health_index_2017:
            health_index_2017[country] = ['Total', h_index]
        if country in health_index_2017:
            avg_index = (health_index_2017[country][1]+h_index)/2
            health_index_2017[country][1] = round(avg_index, 1)
    else:
        if year == '2018':
            if country not in health_index_2018:
                health_index_2018[country] = ['Total', h_index]
            if country in health_index_2018:
                avg_index = (health_index_2018[country][1] + h_index) / 2
                health_index_2018[country][1] = round(avg_index, 1)

print(health_index_2017)
print(health_index_2018)

print('*' * 30)

# - one dict that groups all data by year for Germany >
# germany = {2017: [sex, health_index]}

health_index_germany = {}

for country, sex, year, h_index in dataset:
    if country == 'Germany':
        if year not in health_index_germany:
            health_index_germany[year] = ['Total', h_index]
        if year in health_index_germany:
            avg_index = (health_index_germany[year][1]+h_index)/2
            health_index_germany[year][1] = round(avg_index, 1)

print(health_index_germany)

print('*' * 30)

# - one dict that groups all data by country and year, by using year in the key together with the country name >
# health_index = {‘France_2017’: [year, sex, health_index]}

health_index = {}

for country, sex, year, h_index in dataset:
    health_index_key = country + '_' + year
    if health_index_key not in health_index:
        health_index[health_index_key] = ['Total', h_index]
    if health_index_key in health_index:
        avg_index = (health_index[health_index_key][1] + h_index) / 2
        health_index[health_index_key][1] = round(avg_index, 1)

print(health_index)

print('*' * 30)

# - starting from the previous health_index dict, display only the data where the health_index > 5

health_index_gt_20 = {}

for country, sex, year, h_index in dataset:
    health_index_key = country + '_' + year
    if h_index > 20:
        if health_index_key not in health_index_gt_20:
            health_index_gt_20[health_index_key] = ['Total', h_index]
        if health_index_key in health_index_gt_20:
            avg_index = (health_index_gt_20[health_index_key][1] + h_index) / 2
            health_index_gt_20[health_index_key][1] = round(avg_index, 1)

print(health_index_gt_20.get('Slovenia_2017', 'Average health index is less than 20!'))

print(health_index_gt_20)

print('*' * 30)

# - starting from the previous health_index dict, display only the data where the health_index > 5 and sex is ‘F’

f_health_index_gt_20 = {}

for country, sex, year, h_index in dataset:
    health_index_key = country + '_' + year
    if h_index > 20:
        if sex == 'F':
            if health_index_key not in f_health_index_gt_20:
                f_health_index_gt_20[health_index_key] = [sex, h_index]
            if health_index_key in f_health_index_gt_20:
                avg_index = (f_health_index_gt_20[health_index_key][1] + h_index) / 2
                f_health_index_gt_20[health_index_key][1] = round(avg_index, 1)

# Check if Portugal_2017 is in the dictionary ('Portugal', 'F', '2017', 19.1)
# Check if Germany_2017 is in the dictionary ('Germany', 'F', '2018', 17.1)

print(f_health_index_gt_20.get('Portugal_2017', 'F health index is less than 20!'))
print(f_health_index_gt_20.get('Germany_2017', 'F health index is less than 20!'))

print('*' * 30)

print(f_health_index_gt_20)