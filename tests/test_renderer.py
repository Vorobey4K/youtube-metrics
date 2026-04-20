from models.video_metrics import VideoMetrics
from presentation.console_renderer import ConsoleRenderer
from reports.clickbait import ClickbaitReport


def test_console_renderer_smoke(capsys):
    data = [
        VideoMetrics("A", 20, 30, 0, 0, 0),
        VideoMetrics("B", 25, 35, 0, 0, 0),
    ]

    ConsoleRenderer().render(data, ClickbaitReport())

    out = capsys.readouterr().out

    assert "A" in out
    assert "B" in out
    assert "CTR" in out or "Title" in out
