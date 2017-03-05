from grappa.operator import OperatorTypes, Operator


def test_operator_types(should):
    OperatorTypes | should.be.a('class')

    (OperatorTypes
        | should.have.property('ATTRIBUTE') > should.be.equal.to('attribute'))

    (OperatorTypes
        | should.have.property('ACCESSOR') > should.be.equal.to('accessor'))

    (OperatorTypes
        | should.have.property('MATCHER') > should.be.equal.to('matcher'))


def test_operator(should):
    Operator | should.be.a('class')

    Operator | should.have.property('run') > should.be.a('method')
    Operator | should.have.property('Type') > should.be.equal.to(OperatorTypes)

    (Operator
        | should.have.property('Dsl')
        > should.be.a('module')
        > should.have.attributes('Message', 'Help',
                                 'Reference', 'Description'))

    Operator | should.have.property('kind') > should.be.equal.to('matcher')
    Operator | should.have.property('operators') > should.have.length.of(0)
    Operator | should.have.property('aliases') > should.have.length.of(0)
    Operator | should.have.property('suboperators') > should.have.length.of(0)
    Operator | should.have.property('value')
    Operator | should.have.property('expected')
    Operator | should.have.property('operator_name')
    Operator | should.have.property('subject_message')
    Operator | should.have.property('expected_message')
