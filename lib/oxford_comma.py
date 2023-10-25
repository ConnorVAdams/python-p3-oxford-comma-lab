def oxford_comma(items):
    if len(items) == 1:
        return items[-1]
    elif len(items) == 2:
        return f'{items[-2]} and {items[-1]}'
    elif len(items) > 2:
        last_two = f'{items[-2]}, and {items[-1]}'
        string = f'{", ".join(items[0:-2])}, {last_two}'
        return string

oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"])