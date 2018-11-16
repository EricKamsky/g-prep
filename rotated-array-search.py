
def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1


def test_search_sorted_exists():
    nums = [1, 2, 3, 4, 5, 6]
    index = search(nums, target=4)
    assert index == 3


def test_search_rotated_sorted_exists():
    nums = [3, 4, 5, 6, 1, 2]
    index = search(nums, target=4)
    assert index == 1


def test_search_sorted_not_exists():
    nums = [1, 2, 3, 4, 5, 6]
    index = search(nums, target=9)
    assert index == -1


def test_search_rotated_sorted_not_exists():
    nums = [3, 4, 5, 6, 1, 2]
    index = search(nums, target=9)
    assert index == -1


def test_search_sorted_dupe_exists():
    nums = [1, 2, 3, 4, 5, 5]
    index = search(nums, target=5)
    # first sequential occurrence
    assert index == 4


test_search_sorted_exists()
test_search_rotated_sorted_exists()
test_search_sorted_not_exists()
test_search_rotated_sorted_not_exists()
test_search_sorted_dupe_exists()
