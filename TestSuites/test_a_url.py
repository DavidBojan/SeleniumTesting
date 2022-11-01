def test_url(set_up):
    actual = set_up.current_url
    expected = 'https://the-internet.herokuapp.com/login'
    assert expected == actual, f'Expected: {expected} . Actual: {actual}'
