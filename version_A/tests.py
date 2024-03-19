from version_A.checkout_system import price


def test_prices(items_pricing):
    # Acceptance tests
    assert price(items_pricing, "") == 0
    print("Test with 0 items passed")

    assert price(items_pricing, "A") == 50
    print("Test A passed")

    assert price(items_pricing, "AB") == 80
    print("Test AB passed")

    assert price(items_pricing, "CDBA") == 115
    print("Test CDBA passed")

    assert price(items_pricing, "AA") == 100
    print("Test AA passed")

    assert price(items_pricing, "AAA") == 130
    print("Test AAA passed")

    assert price(items_pricing, "AAAA") == 180
    print("Test AAAA passed")

    assert price(items_pricing, "AAAAA") == 230
    print("Test AAAAA passed")

    assert price(items_pricing, "AAAAAA") == 260
    print("Test AAAAAA passed")

    assert price(items_pricing, "AAAB") == 160
    print("Test AAAB passed")

    assert price(items_pricing, "AAABB") == 175
    print("Test AAABB passed")

    assert price(items_pricing, "AAABBD") == 190
    print("Test AAABBD passed")

    assert price(items_pricing, "DABABA") == 190
    print("Test DABABA passed")