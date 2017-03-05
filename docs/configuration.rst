Configuration
=============

``grappa`` allows a small level of configuration to customize behavior and
error reporting.

Options
-------

- *use_colors* ``bool`` - Defaults to `True` - Enables/disables showing ANSI colored text in error exception messages.
- *show_code* ``bool`` - Defaults to `True` - Enables/disables showing code fragment with the line that originally caused the error in the exception message.
- *debug* ``bool`` - Defaults to `False` - Enables internal debug mode. This would output a lot of stuff into ``stdout``. Only intended to be used for ``grappa`` developers.

New configuration option can be added in the future

Example
-------

.. code-block:: python

    import grappa

    # Disables code output in error messages
    grappa.config.show_code = False
    # Enables colored error messages
    grappa.config.use_colors = True
