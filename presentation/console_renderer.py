from tabulate import tabulate

from reports.base import BaseReport


class ConsoleRenderer:
    def render(self, data, report: BaseReport) -> None:
        table = [report.to_row(row) for row in data]

        print(
            tabulate(
                table,
                headers=report.headers,
                tablefmt="grid",
            )
        )
