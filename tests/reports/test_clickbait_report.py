import pytest

from models.video_metrics import VideoMetrics
from reports.clickbait import ClickbaitReport


@pytest.mark.parametrize(
    "ctr, retention, should_pass",
    [
        (20, 30, True),
        (10, 30, False),
        (20, 50, False),
        (15, 30, False),
        (20, 40, False),
    ],
)
def test_clickbait_filter(ctr, retention, should_pass):
    data = [VideoMetrics("A", ctr, retention, 0, 0, 0)]

    report = ClickbaitReport()
    result = report.generate(data)

    assert (len(result) == 1) is should_pass


def test_clickbait_sorting():
    data = [
        VideoMetrics("A", 20, 30, 0, 0, 0),
        VideoMetrics("B", 25, 30, 0, 0, 0),
        VideoMetrics("C", 18, 30, 0, 0, 0),
    ]

    report = ClickbaitReport()
    result = report.generate(data)

    assert [v.title for v in result] == ["B", "A", "C"]


def test_clickbait_empty():
    data = [
        VideoMetrics("A", 10, 50, 0, 0, 0),
        VideoMetrics("B", 15, 40, 0, 0, 0),
    ]

    report = ClickbaitReport()
    assert report.generate(data) == []


def test_to_row():
    v = VideoMetrics("A", 20, 30, 0, 0, 0)

    report = ClickbaitReport()
    assert report.to_row(v) == ["A", 20, 30]
