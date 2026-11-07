import typer
from pathlib import Path
from typing import Annotated
from rapidfuzz import fuzz
import os

DEFAULT_SUBDIRS = ["open", "closed", "in_progress", "backlog"]
DEFAULT_FIT_DIR = "fit"
DEFAULT_FUZZ_THRESHOLD = 80.0

app = typer.Typer()


@app.command()
def init(path: str = DEFAULT_FIT_DIR):
    """Creates the fit board directory, and the four default statuses.
    At this time, board dir names other then 'fit' are not supported by this tool."""
    p = Path(path)
    for subdir in DEFAULT_SUBDIRS:
        s = p / subdir
        s.mkdir(exist_ok=True)
        (s / ".gitkeep").touch()


@app.command()
def new(
    contents: str,
    priority: Annotated[
        int, typer.Argument(help="Sets the number appearing in front of the filename")
    ] = 0,
    dirpath: Annotated[
        str, typer.Argument(help="Sets the subdir of the fit board to use")
    ] = "open",
    slug: Annotated[
        str | None,
        typer.Argument(
            help="Sets the name given in the filename. By default, uses the first sentence (ending in '.')"
        ),
    ] = None,
):
    """Creates a new FIT ticket."""
    if slug:
        filename = f"{priority:02d}-{slug.replace(" ", "-")}.md"
    else:
        filename = f"{priority:02d}-{contents.split(".")[0].replace(" ", "-")}.md"
    p = Path(f"fit/{dirpath}/{filename}")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contents)

def find_ticket_file_by_name(name: str, nopartial: bool = False) -> Path | None:
    for current_path, _, filenames in os.walk(DEFAULT_FIT_DIR):
        for filename in filenames:
            if filename == ".gitkeep":
                continue
            fuzz_score = fuzz.partial_ratio(filename, name) if not nopartial else fuzz.QRatio(filename, name)
            if fuzz_score > DEFAULT_FUZZ_THRESHOLD:
                return Path(current_path, filename)

@app.command()
def mv(name: str, subdir: str, nopartial: bool = False):
    """Moves a ticket from its current location into a different subdir.
    Unless --nopartial is used, targets the first file that it fuzzy matches."""
    ticketfile = find_ticket_file_by_name(name, nopartial)
    if ticketfile is not None:
        newfile = Path(DEFAULT_FIT_DIR) / subdir / ticketfile.name
        newfile.parent.mkdir(parents=True, exist_ok=True)
        ticketfile.move(newfile)

    print(name)

def main() -> None:
    app()
