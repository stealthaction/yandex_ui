import pytest

WINDOW_SETTING = {"width": 1920, "height": 1080}


def pytest_addoption(parser):
    """Запуск пайтеста с параметрами"""
    parser.addoption(
        "--launch-mode",
        action="store",
        default="headless",
        help="Choose launch mode: headless or head",
        choices=("headless", "head"),
    )