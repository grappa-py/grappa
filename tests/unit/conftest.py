import pytest
from grappa.context import Context


@pytest.fixture(scope='module')
def ctx():
    return Context()
