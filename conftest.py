def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


def pytest_generate_tests(metafunc):
    option_value = metafunc.config.option.browser
    if 'browser' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("browser", [option_value])
