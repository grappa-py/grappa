import grappa
from grappa.engine import Engine


def test_plugin_api(should):
    grappa | should.be.a('module')
    grappa | should.have.property('use') > should.be.a('function')


def test_register_plugin_function(should):
    state = {'called': False}

    def plugin_stub(engine):
        engine | should.be.equal.to(Engine)
        engine | should.have.property('register') > should.be.a('function')
        state['called'] = True

    grappa.use(plugin_stub)
    state | should.be.have.key('called') > should.be.true


def test_register_plugin_method(should):
    state = {'called': False}

    class plugin_stub(object):
        @staticmethod
        def register(engine):
            engine | should.be.equal.to(Engine)
            engine | should.have.property('register') > should.be.a('function')
            state['called'] = True

    grappa.use(plugin_stub)
    state | should.be.have.key('called') > should.be.true
