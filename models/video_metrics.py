from dataclasses import dataclass


@dataclass
class VideoMetrics:
    title: str
    ctr: float
    retention_rate: float
    views: int
    likes: int
    avg_watch_time: float
