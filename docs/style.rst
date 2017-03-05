Assertion Styles
================

``grappa`` is a behavior-oriented library that comes in two flavors: ``expect`` and ``should``.

Both use the same chainable language to construct assertions, but they differ
in the way an assertion is initially constructed by the use of different operators DSL.

The BDD style is exposed through ``expect`` or ``should`` interfaces.
In both scenarios, you chain together natural language assertions.


should
------

The should style allows for the same chainable assertions as the ``expect`` interface,
however it extends each object with a should property to start your chain.

.. code-block:: python

    from grappa import should

    foo = 'bar'
    beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

    foo | should.be.a('string')
    foo | should.equal('bar')
    foo | should.have.length.of(3)
    beverages | should.have.property('tea').with.length.of(3)


expect
------

.. code-block:: python

    from grappa import expect

    foo = 'bar'
    beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

    expect(foo).to.be.a('string')
    expect(foo).to.equal('bar')
    expect(foo).to.have.length.of(3)
    expect(beverages).to.have.property('tea').that.has.length.of(3)


Expect also allows you to include arbitrary messages to prepend to any failed assertions that might occur.

.. code-block:: python

    var answer = 43

    // AssertionError: expected 43 to equal 42.
    expect(answer).to.equal(42)

    // AssertionError: topic [answer]: expected 43 to equal 42.
    expect(answer, 'topic [answer]').to.equal(42)

This comes in handy when being used with non-descript topics such as booleans or numbers.
