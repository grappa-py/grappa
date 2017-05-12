History
=======

v0.1.7 / 2017-05-12
-------------------

  * feat(#33): show available operators on attribute error
  * feat(#36): add allowed assertion attributes on error

v0.1.6 / 2017-04-28
-------------------

* fix(type): expose proper type value if a type value is the expected value
* fix(reporter): use search() instead of match() for line code matching. fix(reporters): escape underscore sequences

v0.1.5 / 2017-04-28
-------------------

* feat(reporters): add code reporter
* feat(operators): add "that_is", "which_is" attribute DSL operators
* refactor(reporter): match additional negation assertions

v0.1.4 / 2017-04-27
-------------------

* feat(reporters): match attribute expressions for proper code line reporting
* feat(equal): enable show_diff report in operator
* fix(index_test): bad file formatting
* refactor(index_test): add error test case
* refactor(index_test): remove commented code
* feat(docs): add context assertion example in tutorial
* feat(docs): add context manager example
* fix(docs): update error exception example
* refactor(docs): update showcase example
* feat(operators): add not_satisfy attribute operator

v0.1.3 / 2017-03-29
-------------------

* feat(docs): add raise exception examples
* refactor(docs): update showcase example
* feat(reporter): normalize value output in subject/expect sections
* feat(docs): update examples and FAQs. feat(operators): add aliases for start/end operator
* feat(docs): add link to grappa-http plugin
* refactor(docs): add operators type section
* refactor(docs): add beta status documentation notice
* feat(docs): update description
* refactor(docs): update status description
* feat(docs): update links

v0.1.2 / 2017-03-26
-------------------

* feat(docs): add matchers supported keyword arguments
* feat(docs): improve descriptions
* feat(operators): improve length operator for access based chaining
* fix(docs): update error custom message example
* feat(docs): improve documentation. adds operators composition section
* fix(setup.py): add author email

v0.1.1 / 2017-03-23
-------------------

* refactor(diff): process expected values as tuple first
* fix(contain): remove print statements
* refactor(core): normalize yielding syntax, add missing documentation
* refactor(core): normalize yielding syntax, add missing documentation
* feat(#26): support disable operator chaining
* feat(#28): better assertion reporting. feat(operators): add index operator
* refactor(reporter): support raw mode with proper indent pretty printing
* refactor(operators): add satisfy/satisfies attribute operators
* feat(diff): consume diff specific subject/expected values
* feat(operators): add is/is_not operator attributes
* refactor(core): isolate reporters per module
* feat(#13, #25): add suboperators support and diff output report
* refactor(docs): update organization name
* refactor(docs): update project image
* refactor(reporter): ignore subject/expected output if empty
* refactor(reporter): show diff if enabled
* feat(docs): add in a nutshell section
* feat(#24, #25): feature enhancements
* feat(docs): add say thanks badge
* refactor(reporter): load value from operator first
* fix(docs): use proper badges
* fix(docs): update type operator examples
* fix(metadata): update
* refactor(test): add chained test for keys
* feat(Makefile): add publish commands

0.1.0 (2017-03-05)
------------------

* First version (beta)
