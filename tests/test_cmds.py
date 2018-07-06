import sys
import pytest
import os
import shutil
from unittest import mock

from izi_grpc import cli


def test_cmd_server(app):
    sys.argv = 'izi_grpc s'.split()
    with mock.patch('izi_grpc.cmds.Server', autospec=True) as mocked:
        assert cli.main() == 0
        mocked.return_value.run.assert_called_with()


def test_cmd_console(app):
    sys.argv = 'izi_grpc c'.split()
    mocked = mock.MagicMock()
    with mock.patch.dict('sys.modules', {'IPython': mocked}):
        assert cli.main() == 0
        assert mocked.embed.called


def test_cmd_generate():
    sys.argv = ('izi_grpc g -I /path/to/protos -I /another/path/to/protos '
                'hello.proto test.proto').split()

    with mock.patch('grpc_tools.protoc.main', return_value=0) as mocked:
        assert cli.main() == 0
        import grpc_tools
        well_known_path = os.path.join(
            os.path.dirname(grpc_tools.__file__), '_proto')
        proto_out = os.path.join(os.getcwd(), 'protos')
        cmd = [
            'grpc_tools.protoc',
            '--proto_path', '/path/to/protos',
            '--proto_path', '/another/path/to/protos',
            '--proto_path', well_known_path,
            '--python_out', proto_out,
            '--grpc_python_out', proto_out,
            'hello.proto',
            'test.proto'
        ]
        mocked.assert_called_with(cmd)


def test_cmd_new():
    shutil.rmtree('tests/myproject', ignore_errors=True)
    sys.argv = ('izi_grpc new tests/myproject'
                ' --skip-git --skip-peewee').split()
    assert cli.main() == 0
    correct_code = """\
    # import myproject_pb2
    # import myproject_pb2_grpc

    # from izi_grpc.servicer import ServicerMeta


    # class MyprojectServicer(myproject_pb2_grpc.MyprojectServicer, metaclass=ServicerMeta):

    #     pass
    """
    with open('./tests/myproject/app/servicers.py', 'r') as f:
        content = f.read()

    from textwrap import dedent
    assert content == dedent(correct_code).rstrip()
    assert not os.path.exists('./tests/myproject/condfigs/default/peewee.py')
    assert os.path.exists('./tests/myproject/app/tasks.py')

    correct_code = """\
    izi_grpc
    cachext
    celery
    raven
    """
    with open('./tests/myproject/requirements.txt', 'r') as f:
        content = f.read()
    assert content == dedent(correct_code)

    shutil.rmtree('tests/myproject')


def test_cmd_job(app):
    with mock.patch('os.getcwd', return_value=app.root_path):
        sys.argv = 'izi_grpc plusone -n 100'.split()
        assert cli.main() is None
        assert app.config.get('NUMBER') == 101
        sys.argv = 'izi_grpc config_hello'.split()
        assert isinstance(cli.main(), cli.JobException)

    class EntryPoint:
        def load(self):
            @cli.jobm.job('xyz')
            def f2():
                app.config['XYZ'] = 'hello'
            return f2

    def new_entry_iter(name):
        return [EntryPoint()]

    with mock.patch('pkg_resources.iter_entry_points', new=new_entry_iter):
        sys.argv = 'izi_grpc xyz'.split()
        assert cli.main() is None
        assert app.config.get('XYZ') == 'hello'


def test_main():
    sys.argv = 'izi_grpc -h'.split()
    with pytest.raises(SystemExit):
        cli.main()
    # no arguments scenes
    sys.argv = ['izi_grpc']
    with pytest.raises(SystemExit):
        cli.main()
