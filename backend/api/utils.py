

def create_report(shopping_cart, ingredients):
    for ingredient in ingredients:
        shopping_cart += (
            f'{ingredient[0].capitalize()}'
            f' - {ingredient[2]} {ingredient[1]}\n'
        )
    return shopping_cart
