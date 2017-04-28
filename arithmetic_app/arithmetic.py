class ArithmeticOperations(object):

    def __init__(self):
        self.operations_list = ['addition', 'subtraction', 'division', 'multiplication']

    def calculate(self, operation, first_value=0, second_value=0):
        if operation in self.operations_list:
            if isinstance(first_value, int) and isinstance(second_value, int):
                try:
                    calculator = getattr(self, operation)
                    calc_result = calculator(first_value, second_value)
                    return calc_result
                except ZeroDivisionError:
                    return "Cannot divide into zero."

    @staticmethod
    def addition(first_value, second_value):
        return first_value + second_value

    @staticmethod
    def subtraction(first_value, second_value):
        return first_value - second_value

    @staticmethod
    def multiplication(first_value, second_value):
        return first_value * second_value

    @staticmethod
    def division(first_value, second_value):
        return first_value / second_value
