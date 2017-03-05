import pytest
from grappa.context import Context
from grappa import should as _should, expect as _expect


@pytest.fixture(scope='module')
def ctx():
    return Context()


@pytest.fixture(scope='module')
def should():
    return _should


@pytest.fixture(scope='module')
def expect():
    return _expect
