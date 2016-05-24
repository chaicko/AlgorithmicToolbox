import pytest
import sys
from io import StringIO


@pytest.fixture()
def mock_stdin(request):
    class MockStdin(StringIO):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def setvalue(self, *args):
            lines = []
            for i, a in enumerate(args):
                s = str(a)
                if isinstance(a, list):
                    s = " ".join((str(x) for x in a))
                if i != len(args) - 1:
                    s += "\n"
                lines.append(s)
            self.writelines(lines)

        def read(self, *args, **kwargs):
            return self.getvalue()

    mock_stdin_ = MockStdin()
    stdin_ = sys.stdin
    sys.stdin = mock_stdin_

    def fin():
        mock_stdin_.flush()
        sys.stdin = stdin_

    request.addfinalizer(fin)
    return mock_stdin_


@pytest.fixture()
def main_runner(request, mock_stdin, capfd):
    def run():
        print(request.params)

    return run
