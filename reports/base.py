from abc import ABC, abstractmethod

from models.video_metrics import VideoMetrics


class BaseReport(ABC):
    @abstractmethod
    def generate(self, data: list[VideoMetrics]) -> list[VideoMetrics]:
        pass

    @abstractmethod
    def to_row(self, item: VideoMetrics) -> list:
        pass