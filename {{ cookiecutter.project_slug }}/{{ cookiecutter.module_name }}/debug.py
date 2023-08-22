import os


def start_debugger(host: str = "0.0.0.0", port: int = 5678) -> None:
    """Start a remote debugger

    Will wait for a client to attach to the debugger if the
    DEBUGGER_WAIT_FOR_ATTACHMENT environment variable is
    set

    Args:
        host: The hostname/IP address to start the remote debugger
        port: The port to expose the remote debugger on
    """
    import debugpy

    wait: bool = os.environ.get("DEBUGGER_WAIT_FOR_ATTACHMENT") is not None

    debugpy.listen((host, port))
    print(f"Remote debugger listening on tcp://{host}:{port}")

    if wait:
        print("Waiting for client to attach to debugger...")
        debugpy.wait_for_client()
        print("Client attachment received!")
