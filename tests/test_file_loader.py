import pytest
from services.file_loader import load_data
from models.video_metrics import VideoMetrics


def test_load_single_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video A,10.5,50,1000,100,5.0\n"
    )

    data = load_data([str(file)])

    assert len(data) == 1
    assert isinstance(data[0], VideoMetrics)
    assert data[0].title == "Video A"
    assert data[0].ctr == 10.5


def test_load_multiple_files(tmp_path):
    file1 = tmp_path / "f1.csv"
    file2 = tmp_path / "f2.csv"

    file1.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video A,10,50,0,0,0\n"
    )
    file2.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
        "Video B,20,30,0,0,0\n"
    )

    data = load_data([str(file1), str(file2)])

    assert [v.title for v in data] == ["Video A", "Video B"]


def test_file_not_found(tmp_path):
    missing = tmp_path / "missing.csv"

    with pytest.raises(ValueError, match="File not found"):
        load_data([str(missing)])


def test_empty_file(tmp_path):
    file = tmp_path / "empty.csv"
    file.write_text(
        "title,ctr,retention_rate,views,likes,avg_watch_time\n"
    )

    assert load_data([str(file)]) == []