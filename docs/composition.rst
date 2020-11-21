Operators composition
=====================

``grappa`` overloads ``|`` and ``>`` operators for expressive assertions composition and chaining.


Pipe operator
-------------

Use ``|`` operator for composing assertions that matches the following conditions:

- For assertion expression initialization.
- A typical `AND` logical composition.
- Assertions that DO tests the same subject.
- Assertions that uses operators that DOES NOT yield a new test subject.

.. code-block:: python

    'foo' | should.have.length.of(3) | should.contain('o')
    [1, 2, 3] | should.be.a(list) | should.have.length.of(3) | should.contain(2)


Arrow operator
--------------

Use ``>`` operator for composing assertions that matches the following conditions:

- For non-initialization assertion expressions.
- A typical `AND` logical composition.
- Assertions that DOES NOT test the same subject.
- Assertions that uses operators that YIELDS a new test subject in the assertion chain.

.. code-block:: python

    [1, 2, 3] | should.be.a(list) > should.have.index.at(2) | should.be.equal.to(3)


Conditional operators
---------------------

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
