import pytest


def test_index(should):
    [1, 2, 3] | should.have.index(2)
    (1, 2, 3) | should.have.index(1)
    (1, 2, 3) | should.have.index(2).to.be.equal(3)

    [1] | should.have.length.of(1).to.have.index.at(0)

    with pytest.raises(AssertionError):
        [1, 2, 3] | should.have.index(4)
