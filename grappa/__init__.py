# -*- coding: utf-8 -*
"""
`grappa` provides two different testing styles: `should` and `expect`.

should
------

Example using ``should`` style::

    from grappa import should

    should('foo').be.equal.to('foo')
    'foo' | should.be.equal.to('foo')

expect
------

Example using ``expect`` style::

    from grappa import expect

    expect([1, 2, 3]).to.contain([2, 3])
    [1, 2, 3] | expect.to.contain([2, 3])


For assertion operators and aliases, see `operators documentation`_.

.. _`operators documentation`: operators.html

Reference
---------
"""

# Export public API module members
from .api import *  # noqa
from .api import __all__  # noqa

# Package metadata
__author__ = 'Tomas Aparicio'
__license__ = 'MIT'

# Current package version
__version__ = '0.1.8'
