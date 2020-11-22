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

**Assertion form**:

.. code-block:: python

    'foo' | should.be.true

.. code-block:: python

    'foo' | expect.to.be.true

**Negation form**:

.. code-block:: python

    'foo' | should.not_be.true

.. code-block:: python

    'foo' | expect.to_not.be.true


false
-----

Asserts if a given subject is `False` value.

=======================  ========================
 **Related operators**   true_
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.be.false

.. code-block:: python

    'foo' | expect.to.be.false

**Negation form**:

.. code-block:: python

    'foo' | should.not_be.false

.. code-block:: python

    'foo' | expect.to_not.be.false


callable
--------

Asserts if a given subject is a callable type or an object that
implements ``__call__()`` magic method.

=======================  ========================
 **Related operators**   implements_
=======================  ========================

**Assertion form**:

.. code-block:: python

    (lambda x: x) | should.be.callable

.. code-block:: python

    (lambda x: x) | expect.to.be.callable

**Negation form**:

.. code-block:: python

    None | should.not_be.callable

.. code-block:: python

    None | expect.to_not.be.callable


empty
-----

Asserts if a given subject is an empty object.

A subject is considered empty if it's ``None``, ``0`` or ``len(subject)``
is equals to ``0``.

=======================  ========================
 **Related operators**   present_ none_
=======================  ========================

**Assertion form**:

.. code-block:: python

    [] | should.be.empty

.. code-block:: python

    tuple() | expect.to.be.empty

**Negation form**:

.. code-block:: python

    [1, 2, 3] | should.not_be.empty

.. code-block:: python

    (1, 2, 3) | expect.to_not.be.empty


none
----

Asserts if a given subject is ``None``.

=======================  ========================
 **Related operators**   present_ empty_
=======================  ========================

**Assertion form**:

.. code-block:: python

    None | should.be.none

.. code-block:: python

    None | expect.to.be.none

**Negation form**:

.. code-block:: python

    'foo' | should.not_be.none

.. code-block:: python

    'foo' | expect.to_not.be.none


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

**Assertion form**:

.. code-block:: python

    'foo' | should.be.present

.. code-block:: python

    'foo' | expect.to.be.present

**Negation form**:

.. code-block:: python

    '' | should.not_be.present

.. code-block:: python

    False | expect.to_not.be.present


.. _`implements`: http://grappa.readthedocs.io/en/latest/matchers-operators.html#implements
