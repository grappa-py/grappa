from grappa.exceptions import GrappaAssertionError


def test_exceptions(should):
    GrappaAssertionError | should.be.a('class')

    # Test assertion instance
    GrappaAssertionError() | should.be.instance.of(AssertionError)

    # Test assertion properties
    err = GrappaAssertionError(error='foo', reasons=['bar'], operator=True)
    err | should.have.property('error') > should.be.equal.to('foo')
    err | should.have.property('reasons') > should.be.equal.to(['bar'])
    err | should.have.property('operator') > should.be.true
