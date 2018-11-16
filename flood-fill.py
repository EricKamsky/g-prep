import copy


BASE_IMAGE = [['w', 'b', 'w', 'b'],
              ['b', 'b', 'b', 'w'],
              ['w', 'b', 'w', 'w'],
              ['w', 'b', 'b', 'w']]


def flood_fill(image, x, y, new_color):
    # flip start cell
    old_color = 'b' if new_color == 'w' else 'w'
    if image[y][x] == old_color:
        image[y][x] = new_color
        # recursively invoke flood fill on all surrounding cells:
        if x > 0:
            flood_fill(image, x-1, y, new_color)
        if x < len(image[y]) - 1:
            flood_fill(image, x+1, y, new_color)
        if y > 0:
            flood_fill(image, x, y-1, new_color)
        if y < len(image) - 1:
            flood_fill(image, x, y+1, new_color)
    return image


def test_flood_fill_black():
    image = copy.deepcopy(BASE_IMAGE)
    x = 0
    y = 3
    new_color = 'b'
    new_image = flood_fill(image, x, y, new_color)
    print(new_image)
    assert new_image == [['w', 'b', 'w', 'b'],
                         ['b', 'b', 'b', 'w'],
                         ['b', 'b', 'w', 'w'],
                         ['b', 'b', 'b', 'w']]


def test_flood_fill_white():
    image = copy.deepcopy(BASE_IMAGE)
    x = 1
    y = 1
    new_color = 'w'
    new_image = flood_fill(image, x, y, new_color)
    print(new_image)
    assert new_image == [['w', 'w', 'w', 'b'],
                         ['w', 'w', 'w', 'w'],
                         ['w', 'w', 'w', 'w'],
                         ['w', 'w', 'w', 'w']]


def test_flood_fill_white2():
    image = copy.deepcopy(BASE_IMAGE)
    x = 3
    y = 0
    new_color = 'w'
    new_image = flood_fill(image, x, y, new_color)
    print(new_image)
    assert new_image == [['w', 'b', 'w', 'w'],
                         ['b', 'b', 'b', 'w'],
                         ['w', 'b', 'w', 'w'],
                         ['w', 'b', 'b', 'w']]


test_flood_fill_black()
test_flood_fill_white()
test_flood_fill_white2()
