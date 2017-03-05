# -*- coding: utf-8 -*-


class Empty(object):
    """
    Empty object represents emptyness state in `grappa`.
    """

    def __repr__(self):
        return 'Empty'

    def __len__(self):
        return 0


# Object reference representing emptpyness
empty = Empty()
