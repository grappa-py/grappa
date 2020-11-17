import pytest
from grappa.test import Test as GrappaTest
from grappa import should, expect


@pytest.mark.parametrize('operator', (
    'to', 'has', 'have', 'include', 'do', 'that', 'which', '_is'
))
def test_assertion_attributes(operator):
    assert isinstance(getattr(should, operator), GrappaTest)
    assert getattr(should, operator)._ctx.negate is False
    assert isinstance(getattr(expect, operator), GrappaTest)
    assert getattr(expect, operator)._ctx.negate is False


@pytest.mark.parametrize('operator', (
    'not_to', 'to_not', 'does_not', 'do_not', '_not',
    'not_have', 'not_has', 'have_not', 'has_not', 'dont'
))
def test_negation_attributes(operator):
    assert isinstance(getattr(should, operator), GrappaTest)
    assert getattr(should, operator)._ctx.negate
    assert isinstance(getattr(expect, operator), GrappaTest)
    assert getattr(expect, operator)._ctx.negate


def test_negation_called_before_non_negation_attributes():
    expect(False).to_not.have.true
    expect(False).not_to.be.true

    False | should.to_not.have.true
    False | should.not_to.be.true