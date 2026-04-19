import csv
import logging
from models.video_metrics import VideoMetrics

logger = logging.getLogger(__name__)


def load_data(files: list[str]) -> list[VideoMetrics]:
    data: list[VideoMetrics] = []

    for file_path in files:
        try:
            with open(file_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    data.append(
                        VideoMetrics(
                            title=row["title"],
                            ctr=float(row["ctr"]),
                            retention_rate=float(row["retention_rate"]),
                            views=int(row["views"]),
                            likes=int(row["likes"]),
                            avg_watch_time=float(row["avg_watch_time"]),
                        )
                    )

        except FileNotFoundError:
            raise ValueError(f"File not found: {file_path}")

    return data