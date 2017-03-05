from ..decorators import attribute


@attribute(operators=('to', 'has', 'have', 'include', 'do'))
def be(ctx):
    """
    Semantic attributes providing chainable declarative DSL
    for assertions.
    """
    ctx.negate = False


@attribute(operators=('that',))
def which(ctx):
    """
    Semantic attributes providing chainable declarative DSL
    for assertions chaning.
    """
    ctx.reset = True


@attribute(operators=(
    'not_to', 'to_not', 'does_not', 'do_not', '_not',
    'not_have', 'not_has', 'have_not', 'has_not', 'dont'
))
def not_be(ctx):
    """
    Semantic negation attributes providing chainable declarative DSL
    for assertions.
    """
    ctx.negate = True
