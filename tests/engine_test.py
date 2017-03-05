from grappa.engine import Engine, isoperator


def test_engine(should):
    Engine | should.be.a('class')
    Engine | should.have.property('register') > should.be.a('function')


class FakeOperator(object):
    operators = tuple()

    kind = 'accessor'

    def run(self):
        pass


def test_isoperator(should):
    FakeOperator() | should.pass_function(isoperator)
