from my_parser import parse_port_range,resolve_hosts,argparse, resolve_host
import pytest


def test_resolve_host_NDD():
    result = resolve_hosts("localhost")

    assert len(result) > 0

    
def test_resolve_host_IP():
    result = resolve_hosts("127.0.0.1")

    assert result ==["127.0.0.1"]

def test_resolve_host_invalid():
    with pytest.raises(ValueError):
        resolve_host("ce-domaine-nexiste-pas-12345.invalid")


def test_parse_port_range():
    result = parse_port_range("1-1024")

    assert result.start == 1
    assert result.stop == 1025

def test_invalid_port_range():
    with pytest.raises(argparse.ArgumentTypeError):
        parse_port_range("abc")

def test_reversed_port_range():
    with pytest.raises(argparse.ArgumentTypeError):
        parse_port_range("1024-1")