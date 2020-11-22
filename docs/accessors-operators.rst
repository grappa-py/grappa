Accessors Operators
===================

These operators do not accept expectation arguments but performs assertion logic.

Example operators: none_, true_, false_, empty_, callable_ ...


true
----

Asserts if a given subject is `True` value.

=======================  ========================
 **Related operators**   false_
=======================  ========================

.. code-block:: python

    'foo' | should.be.true
    'foo' | should.not_be.true

.. code-block:: python

    expect('foo').to.be.true
    expect('foo').to_not.be.true


false
-----

Asserts if a given subject is `False` value.

=======================  ========================
 **Related operators**   true_
=======================  ========================

.. code-block:: python

    'foo' | should.be.false
    'foo' | should.not_be.false

.. code-block:: python

    expect('foo').to.be.false
    expect('foo').to_not.be.false


callable
--------

Asserts if a given subject is a callable type or an object that
implements ``__call__()`` magic method.

=======================  ========================
 **Related operators**   implements_
=======================  ========================

.. code-block:: python

    (lambda x: x) | should.be.callable
    None | should.not_be.callable

.. code-block:: python

    expect(lambda x: x).to.be.callable
    expect(None).to_not.be.callable


empty
-----

Asserts if a given subject is an empty object.

A subject is considered empty if it's ``None``, ``0`` or ``len(subject)``
is equals to ``0``.

=======================  ========================
 **Related operators**   present_ none_
=======================  ========================

.. code-block:: python

    [] | should.be.empty
    [1, 2, 3] | should.not_be.empty

.. code-block:: python

    expect(tuple()).to.be.empty
    expect((1, 2, 3)).to_not.be.empty   


none
----

Asserts if a given subject is ``None``.

=======================  ========================
 **Related operators**   present_ empty_
=======================  ========================

.. code-block:: python

    None | should.be.none
    'foo' | should.not_be.none

.. code-block:: python

    expect(None).to.be.none
    expect('foo').to_not.be.none


exists
------
present
-------

Asserts if a given subject is not ``None`` or a negative value
if evaluated via logical unary operator.

This operator is the opposite of empty_.

=======================  ========================
 **Related operators**   none_ empty_
=======================  ========================

.. code-block:: python

    'foo' | should.be.present
    '' | should.not_be.present

.. code-block:: python

    expect('foo').to.be.present
    expect(False).to_not.be.present


.. _`implements`: http://grappa.readthedocs.io/en/latest/matchers-operators.html#implements
