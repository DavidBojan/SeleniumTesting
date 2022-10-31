def test_url(set_up):
    actual = set_up.current_url
    expected = 'https://the-internet.herokuapp.com/login'
    # expected value, actual value, mesaj in caz de fail
    # set_up.assertEqual(expected, actual, 'URL is incorrect')
    assert expected == actual, f'Expected: {expected} . Actual: {actual}'
