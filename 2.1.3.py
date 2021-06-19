class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, arg):
        if arg > 0:
            super(PositiveList, self).append(arg)
        else:
            raise NonPositiveError
