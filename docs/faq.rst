Frequently Asked Questions
==========================

Can I use ``grappa`` with any testing framework?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, you can. ``grappa`` is testing framework agnostic.
In fact, you don't even need to use a testing framework at all to use it.


Can I extend ``grappa`` with other assertion operators?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Of course you can. ``grappa`` is an extensible modular testing library.

See `creating your custom operator`_ documentation section.


Why use ``grappa`` instead of traditional Python assertions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some people would argue that ``grappa`` is more verbose.
It certainly is, but comes with several benefits that you won't have without it, such as:

- Expressivity: code intentions are more clear, easy to read and understand.
- Readability: besides trivial assertions, it help you writing complex assertions is a human-friendly way.
- Underline complex assertions with an expressive, human-friendly DSL.
- Great error report system with detailed failure reasons, subject/expectation comparison diff, embedded code.
- Lazy evaluation allows ``grappa`` understand what you're expressing in code to perform more fine-grane validations.
- ``grappa`` does type validation under the hood to ensure your providing a valid type.
- ``grappa`` is an extensible assertion layer that can be used in a lot of ways, such as for HTTP protocol testing.
- First-class support for Python data structures assertions and access.


.. _`creating your custom operator`: http://grappa.readthedocs.io/en/latest/plugins.html#creating-operators