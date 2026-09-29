import argparse
import time


from scanner import scan_ports
from render import scan_render
from my_parser import my_parser, parse_port_range

def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner"
    )

    parser.add_argument(
        "host",
        nargs="+",
        help="IP ou NDD  à scanner"
    )

    parser.add_argument(
        "--ports",
        type = range,
        default=parse_port_range("1-1024"),
        help="Plage de ports, par exemple 1-1024"
    )
    parser.add_argument(
        "--timeout",
        type  = float,
        default= 0.5,
        help = "Max time for a scan"
    )
    parser.add_argument(
        "--output",
        default = None,
        help="Name of the output file")
    
    parser.add_argument(
        "--workers",
        type = int,
        default=50,
        help="number of workers"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )


    args = parser.parse_args()

    ips, timeout, workers = my_parser(args, parser)


    for ip in ips:

        start_time = time.perf_counter()

        list_results = scan_ports(ip,args.ports,timeout=timeout,workers=workers)

        elapsed = time.perf_counter() - start_time

        if args.verbose:
            print(f"""
            [*] Scanning {args.host}
            [*] Workers: {args.workers}
            [*] Timeout: {args.timeout}s
            [*] Ports: {args.ports[0]}-{args.ports[-1]}""")
        
        scan_render(args.output,list_results)

        print(f"Scan completed in {elapsed:.2f}s")


if __name__ == "__main__":
    main()