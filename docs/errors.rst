Errors
======

Errors Reporting
----------------

Feedback while testing is key. Seeing errors in your tests is not a nice thing
because informs you something is wrong with your code.
This can even introduce frustration and FUD to developers.

``grappa`` tries to mitigate this by providing a human friendly error reporting
that informs the developer in an intuitive and more effective the following questions:

- what test failed
- what are the reasons of the failure
- what we expect to pass the test
- what we got instead
- where the error actually is (with embedded code)
- how to solve the error
- additional information about the how the assertion works

``grappa`` provides intuitive error reporting for human friendly consumption,
which includes a behavior-oriented

Standard errors vs Grappa errors
--------------------------------

A typical assertion error report using ``nosetests``:

.. code-block:: python

    def test_native_assertion():
        x = [1, 2, 3]
        assert len(x) > 3

.. code-block:: bash

    ======================================================================
    FAIL: tests.should_test.test_should_api
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File ".pyenv/versions/3.6.0/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
    self.test(*self.arg)
    File "grappa/tests/should_test.py", line 11, in test_should_api
    assert len(x) > 3
    AssertionError

Now, a ``grappa`` error report using ``nosetests``:

.. code-block:: python

    def test_grappa_assertion():
    x = [1, 2, 3]
    x | should.be.have.length.of(4)


.. code-block:: bash

    ======================================================================
    FAIL: tests.should_test.test_grappa_assert
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File ".pyenv/versions/3.6.0/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
    self.test(*self.arg)
    File "grappa/tests/should_test.py", line 16, in test_grappa_assert
    x | should.be.have.length.of(4)
    File "grappa/grappa/test.py", line 248, in __ror__
    return self.__overload__(value)
    File "grappa/grappa/test.py", line 236, in __overload__
    return self.__call__(subject, overload=True)
    File "grappa/grappa/test.py", line 108, in __call__
    return self._trigger() if overload else Test(subject)
    File "grappa/grappa/test.py", line 153, in _trigger
    raise err
    AssertionError: Oops! Something went wrong!

    The following assertion was not satisfied
    subject "[1, 2, 3]" should be have length of "4"

    Reasons
    ▸ unexpected object length: 3

    What we expected
    an object that can be length measured and its length is equal to 4

    What we got instead
    an object of type "list" with length 3

    Information
    ▸ An empty object is typically tested via "len(x)"
      built-in function. Most built-in types and objects in Python
      can be tested that way, such as str, list, generator...
      as well as any object that implements "__len__()" method
      and returns "0" as length.
      — Reference: https://docs.python.org/3/library/functions.html#len

    Where
    File "grappa/tests/should_test.py", line 16, in test_grappa_assert

     8|
     9|  def test_native_assert():
    10|      x = [1, 2, 3]
    11|      assert len(x) == 4
    12|
    13|
    14|  def test_grappa_assert():
    15|      x = [1, 2, 3]
    16| >    x | should.be.have.length.of(4)
    17|
    18|
    19|  def test_bool():
    20|      True | should.be.true | should.be.present
    21|      False | should.be.false | should.be.equal.to(False)
    22|      False | should.be.false | should.not_be.equal.to(True)

Error behavior
--------------

``grappa`` raises an standard ``AssertionError`` exception when an assertion is not satisfied,
with some additional properties that provides context data from ``grappa`` for further debugging.

Additional error properties:

- **__grappa__** ``bool`` - Error flag that indicates the error was originated by ``grappa``.
- **error** ``Exception`` - Original exception error, if any.
- **context** ``grappa.Context`` - Current test ``grappa`` context instance. Only for low-level debugging.
