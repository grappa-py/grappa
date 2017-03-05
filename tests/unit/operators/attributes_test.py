import pytest
from grappa.test import Test
from grappa import should, expect


@pytest.mark.parametrize('operator', (
    'to', 'has', 'have', 'include', 'do'
))
def test_assertion_attributes(operator):
    assert isinstance(getattr(should, operator), Test)
    assert getattr(should, operator)._ctx.negate is False
    assert isinstance(getattr(expect, operator), Test)
    assert getattr(expect, operator)._ctx.negate is False


@pytest.mark.parametrize('operator', (
    'which', 'that'
))
def test_chain_attributes(operator):
    assert isinstance(getattr(should, operator), Test)
    assert getattr(expect, operator)._ctx.reset is True
    assert getattr(expect, operator)._ctx.negate is False
    assert isinstance(getattr(expect, operator), Test)
    assert getattr(expect, operator)._ctx.reset is True
    assert getattr(expect, operator)._ctx.negate is False


@pytest.mark.parametrize('operator', (
    'not_to', 'to_not', 'does_not', 'do_not', '_not',
    'not_have', 'not_has', 'have_not', 'has_not', 'dont'
))
def test_negation_attributes(operator):
    assert isinstance(getattr(should, operator), Test)
    assert getattr(should, operator)._ctx.negate
    assert isinstance(getattr(expect, operator), Test)
    assert getattr(expect, operator)._ctx.negate
