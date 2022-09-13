import pytest


@pytest.fixture
def initializable(project):
    return project.security.initializable.library


def test_initializer():

