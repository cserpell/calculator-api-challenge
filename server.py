"""Calculator API challenge."""
import json
import logging

import tornado.ioloop  # Requires tornado
import tornado.log  # Requires tornado
import tornado.web  # Requires tornado


_ALLOWED_OPS = {'+', '-', '*', '/'}
_DEBUG = True


class Error(Exception):
    """Exception raised when input data is wrong for the calculator."""


class CalculatorHandler(tornado.web.RequestHandler):
    """Main handler for this application."""
    def get(self):
        """Returns a hello world string."""
        self.write('Hello, world')

    def data_received(self, chunk):
        """Do nothing.
        @param chunk: streamed request data to process
        """

    def _error(self, message):
        """Writes an error response.
        @param message: string message for logging
        """
        logging.error('Error - %s', message)
        self.set_header('Content-Type', 'application/json')
        self.write('null')

    def _end(self, result):
        """Writes an error response."""
        logging.info('Answering with %s', result)
        self.set_header('Content-Type', 'application/json')
        self.write({'result': result})

    @staticmethod
    def prepare_ops(ops):
        """Convert all input operands into float numbers.
        @param ops: list of values to apply operation
        """
        return [float(one_op) for one_op in ops]

    @staticmethod
    def check_inputs(oop, ops):
        """Check operation is valid and it has at least one operand.
        @param oop: string with valid operation
        @param ops: list of values to apply operation
        """
        if not oop or not ops or oop not in _ALLOWED_OPS:
            raise Error('No operation, no operands or invalid operation')

    @staticmethod
    def apply_op(oop, ops):
        """Get value of calculation.
        @param oop: string with valid operation
        @param ops: list of values to apply operation
        """
        if oop == '+':
            return sum(ops)
        if oop == '-':
            return ops[0] - sum(ops[1:])
        result = ops[0]
        for one_op in ops[1:]:
            if oop == '*':
                result *= one_op
            elif oop == '/':
                result /= one_op
        return result

    def _get_query(self):
        """Get query from URL request."""
        query_str = self.get_body_argument('query', '')
        if not query_str:
            raise Error('No query in request')
        return json.loads(query_str)

    def post(self):
        """Returns a hello world string."""
        try:
            query = self._get_query()
            oop = query.get('op', '')
            ops = query.get('ops', [])
            CalculatorHandler.check_inputs(oop, ops)
            ops = CalculatorHandler.prepare_ops(ops)
            value = CalculatorHandler.apply_op(oop, ops)
        except (Error, ValueError, ZeroDivisionError) as exc:
            self._error(str(exc))
            return
        self._end(str(value))


def make_app(debug):
    """Builds tornado application to run in the server.
    @param debug: boolean, if True, add debug option to application
    """
    logging.info('Starting server')
    tornado.log.enable_pretty_logging()
    return tornado.web.Application([(r'/', CalculatorHandler)], debug=debug)

if __name__ == '__main__':
    make_app(_DEBUG).listen(8888)
    tornado.ioloop.IOLoop.current().start()
