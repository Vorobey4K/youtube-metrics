import argparse
import logging
import sys

from models.video_metrics import VideoMetrics
from presentation.console_renderer import ConsoleRenderer
from reports import REPORTS
from services.file_loader import load_data
from services.logging_config import configure_logging

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate reports from CSV files")

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files",
    )

    parser.add_argument(
        "--report",
        required=True,
        choices=list(REPORTS.keys()),
        help="Report name to generate",
    )

    return parser.parse_args()


def run(data: list[VideoMetrics], report_name: str) -> None:
    logger.info("Report '%s' generation started", report_name)

    report_class = REPORTS[report_name]
    report = report_class()

    result = report.generate(data)

    logger.info("Report '%s' generated with %d rows", report_name, len(result))

    ConsoleRenderer().render(result, report)


def main() -> None:
    configure_logging()

    logger.info("Application started")

    args = parse_args()

    logger.info("Report requested: %s", args.report)
    logger.info("Input files: %s", args.files)

    try:
        data = load_data(args.files)
        logger.info("Loaded %d records", len(data))
    except ValueError:
        logger.exception("Failed to load data from files")
        sys.exit(1)

    run(data, args.report)


if __name__ == "__main__":
    main()
