from models.video_metrics import VideoMetrics
from reports.base import BaseReport


class ClickbaitReport(BaseReport):
    headers = ["Title", "CTR", "Retention Rate"]

    CTR_THRESHOLD = 15
    RETENTION_THRESHOLD = 40

    def generate(self, data: list[VideoMetrics]) -> list[VideoMetrics]:
        filtered = self._filter(data)

        return sorted(
            filtered,
            key=lambda x: x.ctr,
            reverse=True,
        )

    def _filter(self, data: list[VideoMetrics]) -> list[VideoMetrics]:
        return [
            row
            for row in data
            if row.ctr > self.CTR_THRESHOLD
            and row.retention_rate < self.RETENTION_THRESHOLD
        ]

    def to_row(self, item: VideoMetrics) -> list:
        return [item.title, item.ctr, item.retention_rate]
