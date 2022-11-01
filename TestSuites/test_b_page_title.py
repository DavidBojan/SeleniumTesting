from expected_data import ExpectedData

expected_data = ExpectedData()


def test_page_title(set_up):
    page_title = set_up.title
    expected = expected_data.page_title_expected
    assert expected == page_title, f'Expected page title: {expected} . Actual: {page_title}'
