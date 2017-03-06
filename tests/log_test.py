import logging
from grappa import log


def test_log_module(should):
    log | should.be.a('module')

    log | should.have.property('handler')
    log | should.have.property('log') > should.be.instance.of(logging.Logger)

    (log
        | should.have.property('formatter')
        > should.be.instance.of(logging.Formatter))
