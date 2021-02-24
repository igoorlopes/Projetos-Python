def people_with_age_drink(age):
    if age < 14:
        return 'beba toddy'
    elif age < 18:
        return 'beba coca-cola'
    elif age < 21:
        return 'beba cerveja'
    elif age >= 21:
        return 'beba whisky'