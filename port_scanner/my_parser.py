import socket
import argparse


def resolve_hosts(hosts):

    ips = []
    
    if isinstance(hosts, (tuple,list)):

        for host in hosts:
            host_ips = resolve_host(host)

            for ip in host_ips:
                if ip not in ips:
                    ips.append(ip)
    else:
        host_ips = resolve_host(host)

        for ip in host_ips:
            if ip not in ips:
                ips.append(ip)
         
    return ips


def resolve_host(host):
            
        host = host.strip()
        try :

            results = socket.getaddrinfo(host, None)

        except socket.gaierror as e:
                    raise ValueError(f"Impossible de résoudre le domaine : {host}") from e

        ips = []

        for result in results:
            ip = result[4][0]

            if ip not in ips:
                ips.append(ip)
        
        return ips

def parse_port_range(value):
    try:
        start, end = map(int, value.split("-"))
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Port range must have the format START-END"
        )

    if not 1 <= start <= 65535:
        raise argparse.ArgumentTypeError("Invalid start port")

    if not 1 <= end <= 65535:
        raise argparse.ArgumentTypeError("Invalid end port")

    if start > end:
        raise argparse.ArgumentTypeError(
            "Start port must be lower than end port"
        )
    return range(start, end + 1)

def my_parser(args, parser):
    if args.timeout <= 0:
        parser.error("Le timeout doit être supérieur à 0")

    if args.workers <= 0:
        parser.error("Le nombre de workers doit être supérieur à 0")

    
    try:
        ips = resolve_host(args.host)

    except ValueError as e:
        my_parser.error(str(e))

    return ips , args.timeout , args.workers