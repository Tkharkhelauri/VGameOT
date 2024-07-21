from .models import Category, Age

def seeder_func():
    ages = ['12+', '8+', '6+', '16+']
    categories = ['სიტყვების თამაში', 'წვეულების თამაში', 'ლოგიკური თამაში', 'ინტელექტუალური თამაში', 'სამაგიდო თამაში',
                  'ეზოს თამაში', ]

    for age in ages:
        if not Age.objects.filter(age=age):
            new_age = Age(age=age)
            new_age.save()
    for category in categories:
        if not Category.objects.filter(name=category):
            new_category = Category(name=category)
            new_category.save()