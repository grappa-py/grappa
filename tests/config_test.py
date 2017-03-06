import pytest
import grappa
from grappa.config import Config


def test_config(should):
    grappa | should.have.property('config') > should.be.instance.of(Config)

    # Create new config
    conf = Config()

    # Clone
    assert conf.__dict__['opts'] is not grappa.config.__dict__['opts']

    # Setter/getter magic methods
    conf | should.have.property('__setattr__')
    conf | should.have.property('__getattr__')

    # Defaults options
    (conf
        | should.have.property('defaults')
        > should.be.equal.to(grappa.config.defaults))

    # Test define properties
    conf.debug = False
    conf.show_code = True
    conf | should.have.property('debug') > should.be.false
    conf | should.have.property('show_code') > should.be.true

    # Invalid config option should raise an error
    with pytest.raises(ValueError):
        conf.foo = 'bar'
