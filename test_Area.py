import Area



def test_AreaRect():
    x = 5
    y = 10
    result = Area.Area_Rectangle(x, y)
    assert result == x * y


def test_AreaCircle():
    a = 5
    result = Area.Area_circle(a)
    assert result == 3.14 * a * a


def test_PeriRect():
    x = 15
    y = 6
    result = Area.Peri_Rectangle(x, y)
    assert result == 2 * (x + y)


def test_AreaSqr():
    a = 13
    result = Area.Area_Sqr(a)
    assert result == a * a


def test_Areatri():
    x = 15
    y = 10
    result = Area.Area_Triangle(x, y)
    assert result == 0.5 * x * y