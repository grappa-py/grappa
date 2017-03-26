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

Example
^^^^^^^

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

Example
^^^^^^^

.. code-block:: python

    [1, 2, 3] | should.be.a(list) > should.have.index.at(2) | should.be.equal.to(3)
