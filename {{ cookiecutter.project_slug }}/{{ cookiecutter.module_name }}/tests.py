import os
from typing import TYPE_CHECKING

import debugpy

from {{ cookiecutter.module_name }}.debug import start_debugger

if TYPE_CHECKING:
    from pytest_mock.plugin import MockerFixture


def test_debugger_waits_for_client(mocker: "MockerFixture") -> None:
    os.environ["DEBUGGER_WAIT_FOR_ATTACHMENT"] = "1"
    debugpy.wait_for_client = mocker.MagicMock()
    debugpy.listen = mocker.MagicMock()

    start_debugger()

    assert debugpy.listen.called
    assert debugpy.wait_for_client.called
