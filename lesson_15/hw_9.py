def popular_words(text, words):
    text_low = text.lower().split()
    new_dict = {}
    for world in words:
        if world in text_low:
            new_dict[world] = text_low.count(world)
        else:
            new_dict[world] = 0
    return new_dict


assert popular_words('''Hi! When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
