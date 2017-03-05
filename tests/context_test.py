from grappa.context import Context


def test_context(should):
    ctx = Context()

    # Setter/getter magic methods
    ctx | should.have.property('has')
    ctx | should.have.property('__setattr__')
    ctx | should.have.property('__getattr__')

    # Defaults options
    ctx | should.have.property('negate') > should.be.false

    # Test define properties
    ctx.foo = 'bar'
    ctx.bar = True
    ctx | should.have.property('foo') > should.be.equal.to('bar')
    ctx | should.have.property('bar') > should.be.true

    ctx.has('foo') | should.be.true
    ctx.has('baz') | should.be.false

    ctx.__repr__() | should.be.equal.to(
        "{'negate': False, 'foo': 'bar', 'bar': True}")
