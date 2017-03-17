.. image:: http://i.imgur.com/kKZPYut.jpg
   :width: 100%
   :alt: grappa logo
   :align: center


|Build Status| |PyPI| |Coverage Status| |Documentation Status| |Stability| |Quality| |Versions| |SayThanks|

About
-----

``grappa`` is a behavior-oriented, self-declarative, expressive and developer-friendly
lightweight assertion library for Python_.

``grappa`` comes with two declarative `assertion styles`_: ``expect`` and ``should``.

It also comes with a detailed, human-friendly `error reporting`_ system that aims to reduce friction
and improve human agility while testing and fixing software.

To get started, take a look to the `documentation`_, `tutorial`_ and `assertion operators`_.

Status
------

``grappa`` is currently **beta quality** software and under active development and improvements.

API is not stable yet and still prone to introduce breaking changes.

In a nutshell
-------------

Just a small example of `grappa` capabilities:

.. code-block:: python

    from grappa import should

    True | should.be.true
    'bar' | should.be.equal.to('foo')
    13.14 | should.be.higher.than(13)

    {'foo': True} | should.be.a('dict')
    [1, 2, 3] | should.be.a('list') > should.have.length.of(3)
    (lambda x: x) | should.not_be.have.type.of('lambda')

    {'foo': 'bar'} | should.have.key('foo') > should.be.equal('bar')

    an_object | should.have.properties('foo', 'bar', 'baz')
    an_object | should.implement.methods('foo', 'bar', 'baz')

See `documentation`_ for more examples.

Why grappa?
-----------

``grappa`` aims to assist humans while doing a very recurrent and not very fun task in software development: testing things.

The core idea behind ``grappa`` comes from the fact that human time is considerably more expensive than machine time,
and therefore any machine assistance to optimize processes and close the gap is beneficial.

With ``grappa`` you can express almost in plain English what the test contract actually is, but in a way that's
fun and easy to write but also more easy and pleasant to read or maintain by other developers.


The Zen of grappa
-----------------

- Frictionless testing: introducing self-declarative behavior testing patterns can make testing more fun for test writers and more enjoyable for test readers.
- Expressivity is paramount: humans should easily understand what the code is doing.
- Human time is expensive: any modern software should assist people to identify and understand errors easily.
- Make error reporting great again: feedback during testing is key, let's make it more handy and less frustrating.
- Testing patterns consolidation: software expectations are limited to the boundaries of language data types and structures.
- Do not hurt feelings: seeing errors is not a nice thing, but it can be painless if details are showed you in a more gentle way.


Features
--------

-  Behavior-oriented expressive Pythonic fluent API.
-  Provides both ``expect`` and ``should`` assertion styles.
-  Full-featured built-in assertions.
-  Human-friendly and frustration-less error reporting.
-  Composable assertions chaining.
-  Extensible assertions based on third-party plugins.
-  Testing framework agnostic. Works with ``unittest``, ``nosetests``, ``pytest`` ...
-  Lightweight and (almost) dependency-free.
-  Works with Python 2.6+, 3+ and PyPy.


Installation
------------

Using ``pip`` package manager:

.. code-block:: bash

    pip install --upgrade grappa

Or install the latest sources from Github:

.. code-block:: bash

    pip install -e git+git://github.com/grappa-python/grappa.git#egg=grappa


.. _Python: http://python.org
.. _`documentation`: http://grappa.readthedocs.io
.. _`tutorial`: http://grappa.readthedocs.io/en/latest/tutorial.html
.. _`error reporting`: http://grappa.readthedocs.io/en/latest/errors.html
.. _`assertion styles`: http://grappa.readthedocs.io/en/latest/style.html
.. _`assertion operators`: http://grappa.readthedocs.io/en/latest/operators.html

.. |Build Status| image:: https://travis-ci.org/grappa-python/grappa.svg?branch=master
   :target: https://travis-ci.org/grappa-python/grappa
.. |PyPI| image:: https://img.shields.io/pypi/v/grappa.svg?maxAge=2592000?style=flat-square
   :target: https://pypi.python.org/pypi/grappa
.. |Coverage Status| image:: https://coveralls.io/repos/github/grappa-python/grappa/badge.svg?branch=master
   :target: https://coveralls.io/github/grappa-python/grappa?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/grappa/badge/?version=latest
   :target: http://grappa.readthedocs.io/en/latest/?badge=latest
.. |Quality| image:: https://codeclimate.com/github/grappa-python/grappa/badges/gpa.svg
   :target: https://codeclimate.com/github/grappa-python/grappa
   :alt: Code Climate
.. |Stability| image:: https://img.shields.io/pypi/status/grappa.svg
   :target: https://pypi.python.org/pypi/grappa
   :alt: Stability
.. |Versions| image:: https://img.shields.io/pypi/pyversions/grappa.svg
   :target: https://pypi.python.org/pypi/grappa
   :alt: Python Versions
.. |SayThanks| image:: https://img.shields.io/badge/Say%20Thanks!-%F0%9F%A6%89-1EAEDB.svg
   :target: https://saythanks.io/to/h2non
   :alt: Say Thanks
