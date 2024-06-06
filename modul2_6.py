
def single_root_words(root_world, *other_words):
    same_words = []
    for word in other_words:
        if root_world in word or word in root_world:
            root_world.upper()
            root_world.lower()
            word.upper()
            word.lower()
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(*result1)
print(*result2)
