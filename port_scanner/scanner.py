import socket
import time 

from concurrent.futures import ThreadPoolExecutor
from models import PortResult


import socket
import time

def scan_hosts(hosts, ports, timeout=0.5, workers=50):
    results = {}

    for host in hosts:
        results[host] = scan_ports(
            host,
            ports,
            timeout=timeout,
            workers=workers
        )

    return results


def scan_port(host, port, timeout=0.5):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = None

    start = time.perf_counter()

    try:
        result = sock.connect_ex((host, port))
        latency = time.perf_counter() - start

        if result == 0:
            state = "OPEN"

            # Tentative de récupération du banner
            try:
                data = sock.recv(1024)
                banner = data.decode("utf-8", errors="replace").strip()
            except socket.timeout:
                banner = None

        else:
            state = "CLOSED"
            banner = None

        return PortResult(port,state,service,latency,banner)

        

    except socket.timeout:
        return PortResult(port,"TIMEOUT",service,None,None)
 

    except OSError:
        return PortResult(port,"ERROR",service,None,None)

    finally:
        sock.close()



def scan_ports(host,ports,timeout=0.2,workers = 50):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        return list(executor.map(lambda port :scan_port(host, port,timeout),ports))


def scan_ports_udp(host,ports,timeout=0.2,workers = 50):
    with ThreadPoolExecutor(max_workers=workers) as executor:
            return list(executor.map(lambda port :scan_port(host, port,timeout),ports))

     
        

    


                