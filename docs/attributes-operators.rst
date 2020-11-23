Attributes Operators
====================

These operators provides assertion/negation logic.

Example operators: to_, be_ not_be_, which_ ...


Assertion
---------

be
^^
to
^^
has
^^^
have
^^^^
do
^^
include
^^^^^^^
satisfy
^^^^^^^
satisfies
^^^^^^^^^
_is
^^^
which
^^^^^
that
^^^^
that_is
^^^^^^^
which_is
^^^^^^^^

Semantic chainable attributes that defines non-negative assertions.

Typically, you will use them implicitly in order to semantically describe your assertions.

=======================  ========================
 **Assertion mode**      positive
-----------------------  ------------------------
 **Resets context**      no
=======================  ========================

.. code-block:: python

    'foo' | should.be.equal.to('bar')
    'foo' | should.have.length.of(3)

    {'foo': 'bar'} | should.have.key('foo').which.should.be.equal.to('bar')
    {'foo': 'bar'} | should.have.key('foo').that.should.have.length.of(3)

.. code-block:: python

    expect('foo').to.equal.to('bar')
    expect('foo').to.have.length.of(3)

    expect({'foo': 'bar'}).to.have.key('foo').which.expect.to.be.equal('bar')
    expect({'foo': 'bar'}).to.have.key('foo').which.expect.to.have.length.of(3)


Negation
--------

not_be
^^^^^^
not_present
^^^^^^^^^^^
not_to
^^^^^^
to_not
^^^^^^
does_not
^^^^^^^^
do_not
^^^^^^
dont
^^^^
have_not
^^^^^^^^
not_have
^^^^^^^^
has_not
^^^^^^^
not_has
^^^^^^^
that_not
^^^^^^^^
which_not
^^^^^^^^^
is_not
^^^^^^
_not
^^^^
not_satisfy
^^^^^^^^^^^

Semantic chainable attributes that defines negative assertions.

Typically, you will use them implicitly in order to semantically describe your assertions.

=======================  ========================
 **Assertion mode**      negation
-----------------------  ------------------------
 **Resets context**      no
=======================  ========================

.. code-block:: python

    'foo' | should.not_be.equal.to('bar')
    'foo' | should.have_not.length.of(3)

.. code-block:: python

    expect('foo').to_not.equal.to('bar')
    expect('foo').to.not_have.length.of(3)
