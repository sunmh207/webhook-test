import io
import unittest
from contextlib import redirect_stdout

from yanghui import print_yanghui, yanghui


class YanghuiTests(unittest.TestCase):
    def test_yanghui_generates_first_five_rows(self):
        self.assertEqual(
            yanghui(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1],
            ],
        )

    def test_yanghui_zero_rows_returns_empty_list(self):
        self.assertEqual(yanghui(0), [])

    def test_print_yanghui_outputs_expected_rows(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_yanghui(3)

        output_lines = buffer.getvalue().splitlines()
        self.assertEqual(output_lines, ["  1  ", " 1 1 ", "1 2 1"])


if __name__ == "__main__":
    unittest.main()
