from Cats import Cat

cats = [
    {
        "name": "Пушинка",
        "gender": "девочка",
        "age": "1 год"
    },
    {

        "name": "Сэм",
        "gender": "мальчик",
        "age": "2 года"
    },
    {

        "name": "Снежок",
        "gender": "мальчик",
        "age": "4 года"
    }
]

for cat in cats:
    cat_object = Cat(name=cat.get("name"),
                  gender=cat.get("gender"),
                  age=cat.get("age"))
    print(f'Имя: {cat_object.name},\n'
          f'Возраст: {cat_object.age},\n'
          f'Пол: {cat_object.gender}\n')
