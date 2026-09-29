from dataclasses import dataclass

@dataclass
class PortResult:
    port: int
    state: str
    service: str | None
    latency: float | None
    banner: str | None