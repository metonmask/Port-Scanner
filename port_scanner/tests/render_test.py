from scanner import scan_ports, scan_hosts
from render import scan_render
from pathlib import Path


def test_render_csv():

    path = Path("file.csv")


    results = scan_hosts(
        "127.0.0.1",
        range(1, 10),
        timeout=0.5,
        workers=5
    )

    scan_render("file.csv", results)

    assert path.exists()

    path.unlink()
    


def test_render_json():

    path = Path("file.json")


    results = scan_hosts(
        "127.0.0.1",
        range(1, 10),
        timeout=0.5,
        workers=5
    )

    scan_render("file.json", results)

    assert path.exists()

    path.unlink()
