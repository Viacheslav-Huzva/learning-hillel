import csv


def read_data(tech_inventory):
    with open(tech_inventory, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data


def create_category_brand_index(data):
    category_index = {}
    brand_index = {}
    for item in data:
        category = item['category']
        if category not in category_index:
            category_index[category] = []
        category_index[category].append(item)

        brand = item['brand']
        if brand not in brand_index:
            brand_index[brand] = []
        brand_index[brand].append(item)
    return category_index, brand_index


def print_brand_statistics(brands):
    print('Статистика по брендам:')
    for brand in brands:
        print(f"- Від бренду \"{brand}\" є {len(brands[brand])} товарів")


def print_category_statistics(categories):
    print('Статистика по категоріям:')
    for category in categories:
        print(f"- Серед категорії \"{category}\" є {len(categories[category])} товарів")


def print_brand_products(brand_name, brands):
    print(f'Інформація про товари бренду "{brand_name}":')
    for row in brands[brand_name]:
        print(row)


def print_category_products(category_name, categories):
    print(f'Інформація про товари категорії "{category_name}":')
    for row in categories[category_name]:
        print(row)


def print_products_by_brands_in_categories(categories):
    print('Розподіл товарів по брендам для кожної категорії:')
    for category in categories:
        brands_in_category = {}
        for row in categories[category]:
            brand = row['brand']
            if brand not in brands_in_category:
                brands_in_category[brand] = 1
            else:
                brands_in_category[brand] += 1
        print(f"- У категорії \"{category}\" представлені товари таких брендів: ", brands_in_category)


if __name__ == '__main__':
    data = read_data('tech_inventory.csv')
    category_index, brand_index = create_category_brand_index(data)

    print_brand_statistics(brand_index)
    print_category_statistics(category_index)

    selected_brand = 'Samsung'
    print_brand_products(selected_brand, brand_index)

    selected_category = 'Smartphones'
    print_category_products(selected_category, category_index)

    print_products_by_brands_in_categories(category_index)
