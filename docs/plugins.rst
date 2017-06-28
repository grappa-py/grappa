Plugins
=======

Third-party plugins
-------------------

List of third-party plugins for ``grappa``.

**Official plugins**

- `http`_ - HTTP protocol assertions with domain-specific DSL.
- `server`_ - Server/system assertions with domain-specific DSL.

**Community plugins**

Did you create your own plugin? Open an issue or send a Pull Request!


Creating your own plugin
------------------------

Creating operators
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from grappa import Operator

    class MyEqualOperator(Operator):
        """
        MyOperator implements a custom `grappa` assertion operator.

        Operators should inherit from `grappa.Operator` for convenience
        and implement `match()` method.
        """

        # List of operators keywords (required)
        operators = ('equal', 'same', 'eql')

        # Chain DSL aliases (optional)
        aliases = ('to', 'of', 'type', 'as')

        # Expected custom message template (optional)
        expected_message = Operator.Dsl.Message(
            'expected a value that of type "{type}" that is equal to "{value}"',
            'expected a a value that is not equal to "{value}"',
        )

        def match(self, subject, expected, **kw):
            return subject == expected, ['subject is not equal to {}'.format(expected)]


Alternatively, you can create and self-register simple, small operators via decorator:

.. code-block:: python

  import grappa

  @grappa.accessor
  def my_accessor_operator(ctx, subject, **kw):
    return len(subject) > 3, ['subject length must be higher than 3']


.. code-block:: python

  import grappa

  @grappa.matcher
  def my_matcher_operator(ctx, subject, expected, **kw):
    return subject == expected, ['values are not equal']


Registering the plugin
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import grappa

    # Explicitly register operators
    def my_plugin_register(engine):
        engine.register(MyEqualOperator, MyOtherOperator)

    grappa.use(my_plugin_register)


Alternatively, you can self-register your operator classes via ``register`` decorator:

.. code-block:: python

  import grappa

  @grappa.register
  class MyCustomOeprator(grappa.Operator)
    pass


.. _http: https://github.com/grappa-py/http
.. _server: https://github.com/grappa-py/server
