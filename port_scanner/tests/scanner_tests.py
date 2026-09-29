import socket
from scanner import scan_port, scan_ports, scan_hosts
from models import PortResult

def get_unused_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 0))

    port = sock.getsockname()[1]

    sock.close()

    return port


def test_open_port():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 0))
    server.listen(1)

    port = server.getsockname()[1]

    # ton scanner doit détecter ce port
    result = scan_port("127.0.0.1", port)

    assert result.state == "open"

    server.close()

def test_closed_port():
    port = get_unused_port()

    result = scan_port(
        "127.0.0.1",
        port
    )

    assert result.state == "closed"

def test_timeout():
    result = scan_port(
        "127.0.0.1",
        12345,
        timeout=0.1
    )

    assert result.state in {"closed", "timeout"}

def test_scan_ports_returns_port_results():
    results = scan_ports(
        "127.0.0.1",
        range(1, 10),
        timeout=0.5,
        workers=5
    )

    assert all(
        isinstance(result, PortResult)
        for result in results
    )


def test_scan_hosts():

    results = scan_hosts(
        ["127.0.0.1", "192.168.1.1"],
        range(80, 82)
    )

    assert "127.0.0.1" in results and "192.168.1.1" in results

def test_scan_hosts_return_dict():

    results = scan_hosts(
        ["127.0.0.1", "192.168.1.1"],
        range(80, 82)
    )

    assert isinstance(results, dict)