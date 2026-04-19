import sys
import pytest
from main import main


def test_main_success(monkeypatch, capsys, tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video A,20,30,1000,100,5.0\n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", str(file), "--report", "clickbait"],
    )

    main()

    out = capsys.readouterr().out

    assert "Video A" in out


def test_main_file_not_found(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", "missing.csv", "--report", "clickbait"],
    )

    with pytest.raises(SystemExit) as e:
        main()

    assert e.value.code == 1


def test_main_invalid_report(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", "file.csv", "--report", "unknown"],
    )

    with pytest.raises(SystemExit):
        main()