import contextlib
import io
import unittest
from greet import greet, main


def run(argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = main(argv)
    return code, out.getvalue()


class GreetTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_shout(self):
        self.assertEqual(greet("bo", shout=True), "HELLO, BO!")


class CliTest(unittest.TestCase):
    def test_version(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), self.assertRaises(SystemExit) as cm:
            main(["--version"])
        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(out.getvalue(), "greet 0.1.0\n")

    def test_default_cli(self):
        self.assertEqual(run([]), (0, "Hello, world!\n"))

    def test_name_cli(self):
        self.assertEqual(run(["bo"]), (0, "Hello, bo!\n"))

    def test_shout_cli(self):
        self.assertEqual(run(["--shout"]), (0, "HELLO, WORLD!\n"))


if __name__ == "__main__":
    unittest.main()
