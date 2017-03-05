Tutorial
========

Installing grappa
-----------------

Please, see installation_ section.


Importing grappa
----------------

For ``should`` assertion style, use:

.. code-block:: python

    from grappa import should

For ``expect`` assertion style, use:

.. code-block:: python

    from grappa import expect


Basic assertions
----------------

Equality assertions:

.. code-block:: python

    'foo' | should.be.equal.to('foo')

    'foo' | expect.to.be.equal.to('foo')

.. code-block:: python

    [1, 2, 3] | should.be.equal.to([1, 2, 3])

    [1, 2, 3] | expect.to.be.equal.to([1, 2, 3])

Value type assertions:

.. code-block:: python

    1.54 | should.be.a('float')

    1.54 | expect.to.be.a('float')

.. code-block:: python

    'foo' | should.be.a('string')

    'foo' | expect.to.be.a('string')

.. code-block:: python

    [1, 2, 3] | should.be.a('list')

    [1, 2, 3] | expect.to.be.a('list')

Measure length:

.. code-block:: python

    iter([1, 2, 3]) | should.have.length.of(3)

    iter([1, 2, 3]) | expect.to.have.length.of(3)

Custom message errors
---------------------

.. code-block:: python

    [1, 2, 3] | should.have.length.of(2, msg='list must have 2 items')

.. code-block:: python

    'hello world!' | should.have.contain.word('planet', msg='planet word is mandatory')

Negation assertions
-------------------

.. code-block:: python

    'foo' | should.not_be.equal.to('bar')

    'foo' | expect.to_not.be.equal.to('bar')

.. code-block:: python

    [1, 2, 3] | should.not_be.have.length.of('bar')

    'foo' | expect.to_not.be.equal.to('bar')

Featured assertions
-------------------

Dictionary keys assertion

.. code-block:: python

    {'foo': True} | should.have.key('foo')

    {'foo': True} | expect.to.have.key('foo')

.. code-block:: python

    class Foo(object):
        bar = True

        def baz(self):
            pass

    Foo() | should.have.properties('bar', 'baz')

    Foo() | should.have.properties('bar', 'baz')


Conditional assertions
----------------------

``all`` assertion composition, equivalent to ``and`` operator.

You can define ``N`` number of composed assertions.

.. code-block:: python

    {'foo': True} | should.all(should.have.key('foo'), should.have.length.of(1))

    {'foo': True} | expect.all(expect.to.have.key('foo'), expect.to.have.length.of(1))


``any`` assertion composition, equivalent to ``or`` operator.
You can define ``N`` number of composed assertions.

.. code-block:: python

    {'foo': True} | should.any(should.have.key('bar'), should.have.length.of(1))

    {'foo': True} | expect.any(expect.to.have.key('bar'), expect.to.have.length.of(1))


Composing assertions
--------------------

Using ``which``/``that`` attribute operators for chained assertions:

.. code-block:: python

    {'foo': True} | should.have.key('foo').which.should.be.true

    {'foo': True} | expect.to.have.key('foo').that.expect.to.be.true

Using ``|`` for multiple assertions composition (equivalent to ``all``/``and`` composition):

.. code-block:: python

    {'foo': True} | should.be.a('dict') | should.have.key('foo') | should.have.length.of(1)

    {'foo': True} | expect.to.be.a('dict') | expect.to.have.key('foo') | expect.to.have.length.of(1)


Chained assertions
------------------

Using ``>`` operator for chained assertion instead of ``which``/``that`` operators:

.. code-block:: python

    {'foo': True} | should.have.key('foo') > should.be.true

    {'foo': True} | expect.to.have.key('foo') > expect.to.be.true


More complex chained assertions:

.. code-block:: python

    (object
        | should.have.property('foo')
        > should.be.a('tuple')
        > should.have.length.of(3)
        > should.be.equal.to(('foo', 'bar', 'baz')))

.. code-block:: python

    (dictionary
        | should.have.key('foo')
        > should.be.a('list')
        > should.have.length.of(3)
        > should.be.equal.to(['foo', 'bar', 'baz']))


.. _installation: http://grappa.readthedocs.io/en/latest/intro.html#installation
