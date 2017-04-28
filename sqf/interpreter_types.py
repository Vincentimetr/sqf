from sqf.base_type import BaseType
from sqf.types import Code, String, Number, Array, Type


class InterpreterType(BaseType):
    # type that is used by the interpreter (e.g. While type)
    pass


class WhileType(InterpreterType):
    def __init__(self, condition):
        assert(isinstance(condition, Code))
        super().__init__()
        self.condition = condition


class ForType(InterpreterType):
    def __init__(self, variable):
        assert (isinstance(variable, String))
        super().__init__()
        self.variable = variable


class ForSpecType(InterpreterType):
    def __init__(self, array):
        assert (isinstance(array, Array))
        super().__init__()
        self.array = array


class ForFromType(ForType):
    def __init__(self, variable, from_):
        assert (isinstance(from_, Number))
        super().__init__(variable)
        self.from_ = from_


class ForFromToStepType(ForFromType):
    def __init__(self, variable, from_, to, step=Number(1)):
        assert (isinstance(to, Number))
        assert (isinstance(step, Number))
        super().__init__(variable, from_)
        self.to = to
        self.step = step


class SwitchType(InterpreterType):
    def __init__(self, result):
        assert (isinstance(result, Type))
        super().__init__()
        self.result = result