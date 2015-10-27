"""Calculator API challenge unit tests."""
import unittest

import server


class CalculatorHandler(unittest.TestCase):
    """Test CalculatorHandler class."""

    def test_prepare_ops_ok(self):
        """Test prepare_ops with valid input."""
        self.assertListEqual(
            server.CalculatorHandler.prepare_ops([1, 1., '1', '1.']),
            [1., 1., 1., 1.])
        self.assertListEqual(server.CalculatorHandler.prepare_ops([1]), [1.])
        self.assertListEqual(server.CalculatorHandler.prepare_ops([]), [])

    def test_prepare_ops_cannot_parse(self):
        """Test prepare_ops with invalid input."""
        self.assertRaises(ValueError,
                          server.CalculatorHandler.prepare_ops, ['1r'])

    def test_check_inputs_ok(self):
        """Test check_inputs with valid input."""
        server.CalculatorHandler.check_inputs('+', [1.])  # Nothing happens

    def test_check_inputs_operation(self):
        """Test check_inputs with an invalid operation."""
        self.assertRaises(server.Error,
                          server.CalculatorHandler.check_inputs, '', [1.])
        self.assertRaises(server.Error,
                          server.CalculatorHandler.check_inputs, '++', [1.])
        self.assertRaises(server.Error,
                          server.CalculatorHandler.check_inputs, '^', [1.])

    def test_check_inputs_operands(self):
        """Test check_inputs with an invalid list of operands."""
        self.assertRaises(server.Error,
                          server.CalculatorHandler.check_inputs, '+', [])

    def test_apply_op_add(self):
        """Test apply_op for addition."""
        self.assertEqual(server.CalculatorHandler.apply_op('+', [1., 2.]), 3.)
        self.assertEqual(server.CalculatorHandler.apply_op('+', [1.]), 1.)
        self.assertEqual(server.CalculatorHandler.apply_op('+', [1., -1.]), 0.)

    def test_apply_op_sub(self):
        """Test apply_op for substraction."""
        self.assertEqual(server.CalculatorHandler.apply_op('-', [1., 2.]), -1.)
        self.assertEqual(server.CalculatorHandler.apply_op('-', [1.]), 1.)
        self.assertEqual(server.CalculatorHandler.apply_op('-', [1., -1.]), 2.)

    def test_apply_op_prod(self):
        """Test apply_op for product."""
        self.assertEqual(server.CalculatorHandler.apply_op('*', [1., 2.]), 2.)
        self.assertEqual(server.CalculatorHandler.apply_op('*', [1.]), 1.)
        self.assertEqual(server.CalculatorHandler.apply_op('*', [1., -1.]),
                         -1.)

    def test_apply_op_div(self):
        """Test apply_op for division."""
        self.assertEqual(server.CalculatorHandler.apply_op('/', [1., 2.]), 0.5)
        self.assertEqual(server.CalculatorHandler.apply_op('/', [1.]), 1.)
        self.assertEqual(server.CalculatorHandler.apply_op('/', [1., -1.]),
                         -1.)

    def test_apply_op_zero_division(self):
        """Test apply_op fails when dividing by 0."""
        self.assertEqual(server.CalculatorHandler.apply_op('/', [0.]), 0.)
        self.assertRaises(ZeroDivisionError,
                          server.CalculatorHandler.apply_op, '/', [1., 0.])
        self.assertRaises(ZeroDivisionError,
                          server.CalculatorHandler.apply_op, '/', [0., 0.])


if __name__ == '__main__':
    unittest.main()
