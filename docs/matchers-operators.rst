Matchers Operators
==================

These operators does accept expectation arguments and therefore are callable.

Example operators: equal_, within_, start_with_, match_, type_ ...


Generic
-------

equal
^^^^^
same
^^^^

Performs a strict equality comparison between ``x`` and ``y`` values.

Uses ``==`` built-in binary operator for the comparison.

=======================  ========================
 **Chained aliases**     ``value`` ``to`` ``of`` ``as`` ``data``
-----------------------  ------------------------
 **Related operators**   contain_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.be.equal('foo')
    'foo' | should.be.equal.to('foo')
    'foo' | should.be.equal.to.value('foo')

.. code-block:: python

    'foo' | expect.to.equal('foo')
    'foo' | expect.to.equal.to('foo')
    'foo' | expect.to.equal.to.value('foo')

**Negation form**:

.. code-block:: python

    'foo' | should.not_be.equal('foo')
    'foo' | should.not_be.equal.to('foo')
    'foo' | should.not_be.equal.to.value('foo')

.. code-block:: python

    'foo' | expect.to_not.equal('foo')
    'foo' | expect.to_not.equal.to('foo')
    'foo' | expect.to_not.equal.to.value('foo')


contain
^^^^^^^
contains
^^^^^^^^
includes
^^^^^^^^

Asserts if a given value or values can be found in a another object.

=======================  ========================
 **Chained aliases**     ``value`` ``string`` ``text`` ``item`` ``expression`` ``data``
-----------------------  ------------------------
 **Related operators**   equal_ matches_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo bar' | should.contain('bar')
    ['foo', 'bar'] | should.contain('bar')
    ['foo', 'bar'] | should.contain('foo', 'bar')
    [{'foo': True}, 'bar'] | should.contain({'foo': True})

.. code-block:: python

    'foo bar' | expect.to.contain('bar')
    ['foo', 'bar'] | expect.to.contain('bar')
    ['foo', 'bar'] | expect.to.contain('foo', 'bar')
    [{'foo': True}, 'bar'] | expect.to.contain({'foo': True})

**Negation form**:

.. code-block:: python

    'foo bar' | should.do_not.contain('bar')
    ['foo', 'bar'] | should.do_not.contain('baz')

.. code-block:: python

    'foo bar' | expect.to_not.contain('bar')
    ['foo', 'bar'] | expect.to_not.contain('baz')


length
^^^^^^
size
^^^^

Asserts that a given object has exact length.

=======================  ========================
 **Chained aliases**     ``of`` ``equal`` ``to``
-----------------------  ------------------------
 **Related operators**   matches_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.have.length(3)
    [1, 2, 3] | should.have.length.of(3)
    iter([1, 2, 3]) | should.have.length.equal.to(3)

.. code-block:: python

    'foo' | expect.to.have.length(3)
    [1, 2, 3] | expect.to.have.length.of(3)
    iter([1, 2, 3]) | expect.to.have.length.equal.to(3)

**Negation form**:

.. code-block:: python

    'foobar' | should.not_have.length(3)
    [1, 2, 3, 4] | should.not_have.length.of(3)
    iter([1, 2, 3, 4]) | should.not_have.length.equal.to(3)

.. code-block:: python

    'foobar' | expect.to_not.have.length(3)
    [1, 2, 3, 4] | expect.to_not.have.length.of(3)
    iter([1, 2, 3, 4]) | expect.to_not.have.length.equal.to(3)


start_with
^^^^^^^^^^
starts_with
^^^^^^^^^^^

Asserts if a given value starts with a specific items.

=======================  ========================
 **Chained aliases**     ``by`` ``word`` ``number`` ``numbers`` ``item`` ``items`` ``value`` ``char`` ``letter`` ``character``
-----------------------  ------------------------
 **Related operators**   ends_with_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.start_with('f')
    'foo' | should.start_with('fo')
    [1, 2, 3] | should.start_with.number(1)
    iter([1, 2, 3]) | should.start_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with.item('foo')

.. code-block:: python

    'foo' | expect.to.start_with('f')
    'foo' | expect.to.start_with('fo')
    [1, 2, 3] | expect.to.start_with.number(1)
    iter([1, 2, 3]) | expect.to.start_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to.start_with('foo')

**Negation form**:

.. code-block:: python

    'foo' | should.do_not.start_with('o')
    'foo' | should.do_not.start_with('o')
    [1, 2, 3] | should.do_not.start_with(2)
    iter([1, 2, 3]) | should.do_not.start_with.numbers(3, 4)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with('bar')

.. code-block:: python

    'foo' | expect.to_not.start_with('f')
    'foo' | expect.to_not.start_with('fo')
    [1, 2, 3] | expect.to_not.start_with.number(1)
    iter([1, 2, 3]) | expect.to_not.start_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to_not.start_with('foo')


end_with
^^^^^^^^
ends_with
^^^^^^^^^

Asserts if a given value ends with a specific items.

=======================  ========================
 **Chained aliases**     ``by`` ``word`` ``number`` ``numbers`` ``item`` ``items`` ``value`` ``char`` ``letter`` ``character``
-----------------------  ------------------------
 **Related operators**   ends_with_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.ends_with('o')
    'foo' | should.ends_with('oo')
    [1, 2, 3] | should.ends_with.number(3)
    iter([1, 2, 3]) | should.ends_with.numbers(2, 3)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with.item('bar')

.. code-block:: python

    'foo' | expect.to.ends_with('o')
    'foo' | expect.to.ends_with('oo')
    [1, 2, 3] | expect.to.ends_with.number(3)
    iter([1, 2, 3]) | expect.to.ends_with.numbers(2, 3)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to.ends_with('bar')

**Negation form**:

.. code-block:: python

    'foo' | should.do_not.ends_with('f')
    'foo' | should.do_not.ends_with('o')
    [1, 2, 3] | should.do_not.ends_with(2)
    iter([1, 2, 3]) | should.do_not.ends_with.numbers(3, 4)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with('foo')

.. code-block:: python

    'foo' | expect.to_not.ends_with('f')
    'foo' | expect.to_not.ends_with('oo')
    [1, 2, 3] | expect.to_not.ends_with.number(2)
    iter([1, 2, 3]) | expect.to_not.ends_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | expect.to_not.ends_with('foo')


match
^^^^^
matches
^^^^^^^

Asserts if a given string matches a given regular expression.

=======================  ========================
 **Chained aliases**     ``value`` ``string`` ``expression``, ``token``, ``to``, ``regex``, ``regexp``, ``word``, ``phrase``
-----------------------  ------------------------
 **Related operators**   matches_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'hello world' | should.match(r'Hello \w+')
    'hello world' | should.match(r'hello [A-Z]+', re.I))
    'hello world' | should.match.expression(r'hello [A-Z]+', re.I))

.. code-block:: python

    'hello world' | expect.to.match(r'Hello \w+')
    'hello world' | expect.to.match(r'hello [A-Z]+', re.I))
    'hello world' | expect.to.match.expression(r'hello [A-Z]+', re.I))

**Negation form**:

.. code-block:: python

    'hello w0rld' | should.do_not.match(r'Hello \w+')
    'hello w0rld' | should.do_not.match(r'hello [A-Z]+', re.I))
    'hello world' | should.do_not.match.expression(r'hello [A-Z]+', re.I))

.. code-block:: python

    'hello w0rld' | expect.to_not.match(r'Hello \w+')
    'hello w0rld' | expect.to_not.match(r'hello [A-Z]+', re.I))
    'hello world' | expect.to_not.match.expression(r'hello [A-Z]+', re.I))


Collections
-----------

key
^^^
keys
^^^^

Asserts that a given dictionary has a key or keys.

=======================  ========================
 **Chained aliases**     ``present`` ``equal`` ``to``
-----------------------  ------------------------
 **Related operators**   matches_ index_
-----------------------  ------------------------
 **Yields subject**      The key value, if present.
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    {'foo': True} | should.have.key('foo')
    {'foo': True, 'bar': False} | should.have.keys('bar', 'foo')

.. code-block:: python

    {'foo': True} | expect.to.have.key('foo')
    {'foo': True, 'bar': False} | expect.to.have.keys('bar', 'foo')

**Negation form**:

.. code-block:: python

    {'bar': True} | should.not_have.key('foo')
    {'baz': True, 'bar': False} | should.not_have.keys('bar', 'foo')

.. code-block:: python

    {'bar': True} | expect.to_not.have.key('foo')
    {'baz': True, 'bar': False} | expect.to_not.have.keys('bar', 'foo')


index
^^^^^

Asserts that a given iterable has an item in a specific index.

=======================  ========================
 **Chained aliases**     ``present`` ``exists`` ``at``
-----------------------  ------------------------
 **Related operators**   property_ key_ contain_
-----------------------  ------------------------
 **Yields subject**      Value at the selected index, if present.
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    [1, 2, 3] | should.have.index(2)
    [1, 2, 3] | should.have.index(1)
    [1, 2, 3] | should.have.index.at(1)
    [1, 2, 3] | should.have.index.present(1)
    [1, 2, 3] | should.have.index.at(1).equal.to(2)
    [1, 2, 3] | should.have.index.at(1) > should.be.equal.to(2)

.. code-block:: python

    [1, 2, 3] | expect.to.have.index(2)
    [1, 2, 3] | expect.to.have.index.at(1)
    [1, 2, 3] | expect.to.have.index.at(1).equal.to(2)
    [1, 2, 3] | expect.to.have.index.at(1) > expect.be.equal.to(2)

**Negation form**:

.. code-block:: python

    [1, 2, 3] | should.not_have.index(4)
    [1, 2, 3] | should.not_have.index.at(4)
    [1, 2, 3] | should.not_have.index.at(1).to_not.equal.to(5)

.. code-block:: python

    [1, 2, 3] | expect.to_not.have.index(2)
    [1, 2, 3] | expect.to_not.have.index.at(1)
    [1, 2, 3] | expect.to_not.have.index.at(1).equal.to(2)


Numbers
-------

below
^^^^^
lower
^^^^^
less
^^^^

Asserts if a given number is below to another number.

=======================  ========================
 **Chained aliases**     ``of`` ``to`` ``than`` ``number``
-----------------------  ------------------------
 **Related operators**   within_ above_ above_or_equal_ below_or_equal_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    3 | should.be.below(5)
    3 | should.be.below.of(5)
    3 | should.be.below.to(5)
    3 | should.be.less.than(5)
    3 | should.be.lower.than(5)
    3 | should.be.below.to.number(5)
    3 | should.be.below.than.number(5)

.. code-block:: python

    3 | expect.to.be.below(5)
    3 | expect.to.be.below.of(5)
    3 | expect.to.be.below.to(5)
    3 | expect.to.be.less.than(5)
    3 | expect.to.be.lower.than(5)
    3 | expect.to.be.below.to.number(5)
    3 | expect.to.be.below.than.number(5)

**Negation form**:

.. code-block:: python

    5 | should.not_be.below(3)
    5 | should.not_be.below.of(3)
    3 | should.not_be.below.to(5)
    3 | should.not_be.lower.than(5)
    5 | should.not_be.below.to.number(3)

.. code-block:: python

    5 | expect.to_not.be.below(3)
    5 | expect.to_not.be.below.of(3)
    5 | expect.to_not.be.below.than(3)
    5 | expect.to_not.be.below.to.number(3)
    5 | expect.to_not.be.below.than.number(3)


above
^^^^^
higher
^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chained aliases**     ``of`` ``to`` ``than`` ``number``
-----------------------  ------------------------
 **Related operators**   within_ below_ below_or_equal_ above_or_equal_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    5 | should.be.above(3)
    5 | should.be.above.of(3)
    5 | should.be.above.to(3)
    5 | should.be.higher.than(3)
    5 | should.be.above.to.number(3)
    5 | should.be.above.than.number(3)

.. code-block:: python

    5 | expect.to.be.above(3)
    5 | expect.to.be.above.of(3)
    5 | expect.to.be.above.to(3)
    5 | expect.to.be.higher.than(3)
    5 | expect.to.be.above.to.number(3)
    5 | expect.to.be.above.than.number(3)

**Negation form**:

.. code-block:: python

    3 | should.not_be.above(5)
    3 | should.not_be.above.of(5)
    3 | should.not_be.above.to(5)
    3 | should.not_be.higher.than(5)
    3 | should.not_be.above.to.number(5)
    3 | should.not_be.above.than.number(5)

.. code-block:: python

    3 | expect.not_to.be.above(5)
    3 | expect.not_to.be.above.of(5)
    3 | expect.not_to.be.above.to(5)
    3 | expect.not_to.be.higher.than(5)
    3 | expect.not_to.be.above.to.number(5)
    3 | expect.not_to.be.above.than.number(5)


least
^^^^^
above_or_equal
^^^^^^^^^^^^^^
higher_or_equal
^^^^^^^^^^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chained aliases**     ``of`` ``to`` ``than`` ``number``
-----------------------  ------------------------
 **Related operators**   within_ below_ below_or_equal_ above_or_equal_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    3 | should.be.least(3)
    3 | should.be.above_or_equal(3)
    3 | should.be.above_or_equal.of(3)
    3 | should.be.above_or_equal.to(3)
    3 | should.be.higher_or_equal.than(3)
    3 | should.be.above_or_equal.to.number(3)
    3 | should.be.above_or_equal.than.number(3)

.. code-block:: python

    3 | expect.to.be.least(3)
    3 | expect.to.be.above_or_equal(3)
    3 | expect.to.be.above_or_equal.of(3)
    3 | expect.to.be.above_or_equal.to(3)
    3 | expect.to.be.higher_or_equal.than(3)
    3 | expect.to.be.above_or_equal.to.number(3)
    3 | expect.to.be.above_or_equal.than.number(3)

**Negation form**:

.. code-block:: python

    3 | should.not_be.least(3)
    3 | should.not_be.above_or_equal(5)
    3 | should.not_be.above_or_equal.of(5)
    3 | should.not_be.above_or_equal.to(5)
    3 | should.not_be.higher_or_equal.than(5)
    3 | should.not_be.higher_or_equal.to.number(5)
    3 | should.not_be.higher_or_equal.than.number(5)

.. code-block:: python

    3 | expect.not_be.least(3)
    3 | expect.not_be.above_or_equal(5)
    3 | expect.not_be.above_or_equal.of(5)
    3 | expect.not_be.above_or_equal.to(5)
    3 | expect.not_be.higher_or_equal.than(5)
    3 | expect.not_be.higher_or_equal.to.number(5)
    3 | expect.not_be.higher_or_equal.than.number(5)


most
^^^^
below_or_equal
^^^^^^^^^^^^^^
lower_or_equal
^^^^^^^^^^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chained aliases**     ``of`` ``to`` ``than`` ``number``
-----------------------  ------------------------
 **Related operators**   within_ below_ above_ below_or_equal_ above_or_equal_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    3 | should.be.most(3)
    3 | should.be.below_or_equal(3)
    3 | should.be.below_or_equal.of(3)
    3 | should.be.below_or_equal.to(3)
    3 | should.be.lower_or_equal.than(3)
    3 | should.be.lower_or_equal.to.number(3)
    3 | should.be.lower_or_equal.than.number(3)

.. code-block:: python

    3 | expect.to.be.most(3)
    3 | expect.to.be.below_or_equal(3)
    3 | expect.to.be.below_or_equal.of(3)
    3 | expect.to.be.below_or_equal.to(3)
    3 | expect.to.be.lower_or_equal.than(3)
    3 | expect.to.be.lower_or_equal.to.number(3)
    3 | expect.to.be.lower_or_equal.than.number(3)

**Negation form**:

.. code-block:: python

    3 | should.not_be.most(5)
    3 | should.not_be.below_or_equal(5)
    3 | should.not_be.below_or_equal.of(5)
    3 | should.not_be.below_or_equal.to(5)
    3 | should.not_be.lower_or_equal.than(5)
    3 | should.not_be.lower_or_equal.to.number(5)
    3 | should.not_be.lower_or_equal.than.number(5)

.. code-block:: python

    3 | expect.not_be.most(5)
    3 | expect.not_be.below_or_equal(5)
    3 | expect.not_be.below_or_equal.of(5)
    3 | expect.not_be.below_or_equal.to(5)
    3 | expect.not_be.lower_or_equal.than(5)
    3 | expect.not_be.lower_or_equal.to.number(5)
    3 | expect.not_be.lower_or_equal.than.number(5)


within
^^^^^^
between
^^^^^^^

Asserts that a number is within a range.

=======================  ========================
 **Chained aliases**     ``to`` ``numbers`` ``range``
-----------------------  ------------------------
 **Related operators**   below_ above_ above_or_equal_ below_or_equal_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    4 | should.be.within(2, 5)
    5 | should.be.between(2, 5)
    4.5 | should.be.within(4, 5)

.. code-block:: python

    4 | should.not_be.within(2, 5)
    5 | should.not_be.between(2, 5)
    4.5 | should.not_be.within(4, 5)

**Negation form**:

.. code-block:: python

    4 | expect.to.be.within(2, 5)
    5 | expect.to.be.between(2, 5)
    4.5 | expect.to.be.within(4, 5)

.. code-block:: python

    4 | expect.to_not.be.within(2, 5)
    5 | expect.to_not.be.between(2, 5)
    4.5 | expect.to_not.be.within(4, 5)


Objects
-------

a
^
an
^^
type
^^^^
types
^^^^^
instance
^^^^^^^^

Asserts if a given object satisfies a type.
You can use both a type alias string or a ``type`` object.

Supported type aliases:

- string
- int
- integer
- number
- object
- float
- bool
- boolean
- complex
- list
- dict
- dictionary
- tuple
- set
- array
- lambda
- generator
- asyncgenerator
- class
- method
- module
- function
- coroutine
- generatorfunction
- generator function
- coroutinefunction

=======================  ========================
 **Chained aliases**     ``type`` ``types`` ``to`` ``of``, ``equal``
-----------------------  ------------------------
 **Related operators**   equal_ matches_ implements_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    1 | should.be.an('int')
    1 | should.be.an('number')
    True | should.be.a('bool')
    True | should.be.type(bool)
    'foo' | should.be.a(str)
    'foo' | should.be.a('string')
    [1, 2, 3] | should.be.a('list')
    [1, 2, 3] | should.have.type.of(list)
    (1, 2, 3) | should.be.a('tuple')
    (1, 2, 3) | should.have.type.of(tuple)
    (lamdba x: x) | should.be.a('lambda')
    'foo' | should.be.instance.of('string')
    'foo' | expect.be.types('string', 'int')

.. code-block:: python

    1 | expect.to.be.an('int')
    1 | expect.to.be.an('number')
    True | expect.to.be.a('bool')
    True | expect.to.be.type(bool)
    'foo' | expect.to.be.a(str)
    'foo' | expect.to.be.a('string')
    [1, 2, 3] | expect.to.be.a('list')
    [1, 2, 3] | expect.to.have.type.of(list)
    (1, 2, 3) | expect.to.be.a('tuple')
    (1, 2, 3) | expect.to.have.type.of(tuple)
    (lamdba x: x) | expect.to.be.a('lambda')
    'foo' | expect.to.be.instance.of('string')
    'foo' | expect.to.be.types('string', 'int')

**Negation form**:

.. code-block:: python

    1 | should.not_be.an('int')
    1 | should.not_be.an('number')
    True | should.not_be.a('bool')
    True | should.not_be.type(bool)
    'foo' | should.not_be.a(str)
    'foo' | should.not_be.a('string')
    [1, 2, 3] | should.not_be.a('list')
    [1, 2, 3] | should.have_not.type.of(list)
    (1, 2, 3) | should.not_be.a('tuple')
    (1, 2, 3) | should.have_not.type.of(tuple)
    (lamdba x: x) | should.not_be.a('lambda')
    'foo' | should.not_to.be.instance.of('string')
    'foo' | should.not_to.be.types('string', 'int')

.. code-block:: python

    1 | expect.to_not.be.an('int')
    1 | expect.to_not.be.an('number')
    True | expect.to_not.be.a('bool')
    True | expect.to_not.be.type(bool)
    'foo' | expect.to_not.be.a(str)
    'foo' | expect.to_not.be.a('string')
    [1, 2, 3] | expect.to_not.be.a('list')
    [1, 2, 3] | expect.to_not.have.type.of(list)
    (1, 2, 3) | expect.to_not.be.a('tuple')
    (1, 2, 3) | expect.to_not.have.type.of(tuple)
    (lamdba x: x) | expect.to_not.be.a('lambda')
    'foo' | expect.to.not_to.be.instance.of('string')
    'foo' | expect.to.not_to.be.types('string', 'int')


property
^^^^^^^^^
properties
^^^^^^^^^^
attribute
^^^^^^^^^
attributes
^^^^^^^^^^

Asserts if a given object has property or properties.

=======================  ========================
 **Chained aliases**     ``present`` ``equal`` ``to``
-----------------------  ------------------------
 **Related operators**   matches_
-----------------------  ------------------------
 **Yields subject**      The attribute value, if present.
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================


implements
^^^^^^^^^^
implement
^^^^^^^^^
interface
^^^^^^^^^

Asserts if a given object implements an interface of methods.

=======================  ========================
 **Chained aliases**     ``interface`` ``method`` ``methods``
-----------------------  ------------------------
 **Related operators**   matches_
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    Foo() | should.implements('bar')
    Foo() | should.implements.method('bar')
    Foo() | should.implement.methods('bar', 'baz')
    Foo() | should.implement.interface('bar', 'baz')
    Foo() | should.satisfies.interface('bar', 'baz')

.. code-block:: python

    Foo() | expect.to.implement('bar')
    Foo() | expect.to.implement.method('bar')
    Foo() | expect.to.implement.methods('bar', 'baz')
    Foo() | expect.to.implement.interface('bar', 'baz')
    Foo() | expect.to.satisfy.interface('bar', 'baz')

**Negation form**:

.. code-block:: python

    Foo() | should.do_not.implements('bar')
    Foo() | should.do_not.implement.methods('bar', 'baz')
    Foo() | should.do_not.implement.interface('bar', 'baz')
    Foo() | should.do_not.satisfy.interface('bar', 'baz')

.. code-block:: python

    Foo() | expect.to_not.implement('bar')
    Foo() | expect.to_not.implement.method('bar')
    Foo() | expect.to_not.implement.methods('bar', 'baz')
    Foo() | expect.to_not.implement.interface('bar', 'baz')
    Foo() | expect.to_not.satisfy.interface('bar', 'baz')

**Assertion form**:

.. code-block:: python

    Foo() | should.have.property('bar')
    Foo() | should.have.properties('bar', 'baz')
    Foo() | should.have.properties.present.equal.to('bar', 'baz')

.. code-block:: python

    Foo() | expect.to_not.have.property('bar')
    Foo() | expect.to_not.have.properties('bar', 'baz')
    Foo() | expect.to_not.have.properties.present.equal.to('bar', 'baz')

**Negation form**:

.. code-block:: python

    Foo() | should.have_not.property('bar')
    Foo() | should.have_not.properties('bar', 'baz')
    Foo() | should.have_not.properties.present.equal.to('bar', 'baz')

.. code-block:: python

    Foo() | expect.to_not.have.property('bar')
    Foo() | expect.to_not.have.properties('bar', 'baz')
    Foo() | expect.to_not.have.properties.present.equal.to('bar', 'baz')


Exceptions
----------

raises
^^^^^^
raise_error
^^^^^^^^^^^
raises_errors
^^^^^^^^^^^^^

Asserts if a given function raises an exception. The function must be a zero
arity function (no arguments). If you need to pass arguments into your function
you can use ``functools.partial`` to create a zero arity function with your
arguments

=======================  ========================
 **Chained aliases**     ``to`` ``that`` ``are`` ``instance`` ``of``
-----------------------  ------------------------
 **Related operators**   matches_
-----------------------  ------------------------
 **Yields subject**      Message of the exception, if present or joined exception arguments.
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    fn | should.raise_error()
    fn | should.raise_error(ValueError)
    fn | should.raise_error(AttributeError, ValueError)
    fn | should.raise_error(ValueError) > should.equal('File not found')
    fn | should.raise_error(ValueError) > should.contain('not found')

.. code-block:: python

    fn | expect.to.raise_error()
    fn | expect.to.raise_error(ValueError)
    fn | expect.to.raise_error(AttributeError, ValueError)
    fn | expect.to.raise_error(ValueError) > should.equal('File not found')
    fn | expect.to.raise_error(ValueError) > should.contain('not found')

**Negation form**:

.. code-block:: python

    fn | should.do_not.raise_error()
    fn | should.do_not.raise_error(ValueError)
    fn | should.do_not.raise_error(AttributeError, ValueError)

.. code-block:: python

    fn | expect.to_not.raise_error()
    fn | expect.to_not.raise_error(ValueError)
    fn | expect.to_not.raise_error(AttributeError, ValueError)


Predicates
----------

pass_test
^^^^^^^^^
pass_function
^^^^^^^^^^^^^

Asserts if a given subject is valid when passed to a predicate function.

=======================  ========================
 **Chained aliases**     -
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    'foo' | should.pass_test(lambda x: len(x) > 2)
    [1, 2, 3] | should.pass_function(lambda x: 2 in x)

.. code-block:: python

    'foo' | expect.to.pass_test(lambda x: len(x) > 2)
    [1, 2, 3] | expect.to.pass_function(lambda x: 2 in x)

**Negation form**:

.. code-block:: python

    'foo' | should.do_not.pass_test(lambda x: len(x) > 3)
    [1, 2, 3] | should.do_not.pass_function(lambda x: 5 in x)

.. code-block:: python

    'foo' | expect.to_not.pass_test(lambda x: len(x) > 3)
    [1, 2, 3] | expect.to_not.pass_function(lambda x: 5 in x)

Mocks
-----

Required implementation of a mock subject is based on `unittest.mock.Mock`_ class.

To be compatible with ``grappa``, mocks must only implement:

- **called**: a boolean property which indicates whether the mock has been called, or not.
- **call_count**: an integer property which indicates the number of times the mock has been called.
- **assert_called_with(*args, **kwargs)**: a function which raises an ``AssertionError`` when the mock has not been called with given arguments.
- **assert_called_once_with(*args, **kwargs)**: a function which raises an ``AssertionError`` when the mock has not been called with given arguments.


.. warning::

    Mock matchers are not (yet) compatible with piping (|) assertion style.


been_called
^^^^^^^^^^^

Asserts if a given mock subject have been called at least once.

=======================  ========================
 **Optional keywords**   ``msg: str``
=======================  ========================

.. code-block:: python

    expect(mock).to.have.been_called

    expect(mock).to.have_not.been_called


been_called_once
^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called only once.

=======================  ========================
 **Optional keywords**   ``msg: str``
=======================  ========================

.. code-block:: python

    expect(mock).to.have.been_called_once

    expect(mock).to.have_not.been_called_once


been_called_times
^^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called n times.

=======================  ========================
 **Optional keywords**   ``msg: str``
=======================  ========================

**Assertion form**:

.. code-block:: python

    expect(mock).to.have.been_called_times(0)

    expect(mock).to.have_not.been_called_times(3)



been_called_with
^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called at least once
with specified arguments.

=======================  ========================
 **Optional keywords**   ``msg: str``
=======================  ========================

.. code-block:: python

    expect(mock).to.have.been_called_with('foo')
    expect(mock).to.have.been_called_with('foo', True, 150)

    expect(mock).to.have_not.been_called_with('bar', False)


been_called_once_with
^^^^^^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called only once
with specified arguments.

=======================  ========================
 **Optional keywords**   ``msg: str``
=======================  ========================

.. code-block:: python

    expect(mock).to.have.been_called_once_with('foo')
    expect(mock).to.have.been_called_once_with('foo', True, 150)

    expect(mock).to.have_not.been_called_once_with('bar', False)


.. _`unittest.mock.Mock`: https://docs.python.org/3/library/unittest.mock.html#the-mock-class
