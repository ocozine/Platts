import pytest

from projects.homework11.fruit_formal import get_formal_name 
#(part2 of hw)I ran this code but changed homework11.fruit_formal to homework11.fruit_formal_improved and one of my tests did not pass

def test_valid_fruit():
    #testing to make sure all these fruits are in the dictionary as well as their formal name adsa 
    assert get_formal_name('apple') == 'Malus domestica'
    assert get_formal_name('banana') == 'Musa acuminata'
    assert get_formal_name('orange') == 'Citrus × sinensis'
    assert get_formal_name('strawberry') == 'Fragaria × ananassa'
    assert get_formal_name('grape') == 'Vitis vinifera'
    assert get_formal_name('pineapple') == 'Ananas comosus'
    assert get_formal_name('mango') == 'Mangifera indica'
    assert get_formal_name('blueberry') == 'Vaccinium corymbosum'
    assert get_formal_name('peach') == 'Prunus persica'
    assert get_formal_name('watermelon') == 'Citrullus lanatus'
    assert get_formal_name('cherry') == 'Prunus avium'
    assert get_formal_name('pear') == 'Pyrus'
    assert get_formal_name('plum') == 'Prunus domestica'
    assert get_formal_name('raspberry') == 'Rubus idaeus'
    assert get_formal_name('kiwi') == 'Actinidia deliciosa'
    assert get_formal_name('lemon') == 'Citrus limon'
    assert get_formal_name('avocado') == 'Persea americana'
    assert get_formal_name('pomegranate') == 'Punica granatum'
    assert get_formal_name('cranberry') == 'Vaccinium macrocarpon'
    assert get_formal_name('grapefruit') == 'Citrus × paradisi'

def test_invalid_fruit():
    #testidng to see possible inputs that do not exist in dictionary which will produce a 'Unknown'
    assert get_formal_name('boba') == 'Unknown'
    assert get_formal_name('cucumbers') == 'Unknown'
    assert get_formal_name('durian') == 'Unknown'
    assert get_formal_name('') == 'Unknown'
    assert get_formal_name('!') == 'Unknown'

if __name__ == "__main__":
    pytest.main()