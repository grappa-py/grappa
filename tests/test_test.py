import pytest


def test_context_manager(should):
    'foo' | should.to.be.equal('foo')

    with should('foo'):
        should.be.equal('foo')
        should.have.length.of(3)
        should.have.type('string')

    with should('foo'):
        should.be.a('string').which.has.length.of(3)
        should.be.equal('foo')

    should('foo').be.equal('foo')
    'foo' | should.be.equal('foo')

    with pytest.raises(AssertionError):
        with should('foo'):
            should.be.equal('foo')
            should.have.length.of(5)


def test_all_assertions(should):
    'foo' | should.all(should.be.a('string'), should.have.length.to(3))

    'foo' | should.any(should.be.a('number'), should.have.length.to(3))

    with pytest.raises(AssertionError):
        'foo' | should.all(should.be.a('string'), should.have.length.to(5))

    with pytest.raises(AssertionError):
        'foo' | should.any(should.be.a('number'), should.have.length.to(5))


def test_assertion_chaining(should):
    'foo' | should.have.length.between.range(2, 5)

    ('foo'
        | should.have.length.lower.than(4)
        | should.have.length.higher.than(2))

    with pytest.raises(AssertionError):
        'foo' | should.have.length.lower.than(4) | should.have.length.higher(5)


def test_custom_message_error(should):
    with pytest.raises(AssertionError) as err:
        'foo' | should.be.equal('bar', msg='invalid string')

    str(err.value) | should.contain('invalid string')
