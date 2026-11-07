import typer
from pathlib import Path
from typing import Annotated
from rapidfuzz import fuzz
import os
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.padding import Padding
from rich.pretty import Pretty
from rich.rule import Rule
import frontmatter

DEFAULT_SUBDIRS = ["open", "closed", "in_progress", "backlog"]
DEFAULT_FIT_DIR = "fit"
DEFAULT_FUZZ_THRESHOLD = 80.0

SORT_ORDER = ["in_progress", "open", "backlog", "closed"]
FORMATTED_SORT_ORDER = ["[bold green]In Progress[/bold green]", "[bold blue]Open[/bold blue]", "[bold purple]Backlog[/bold purple]", "[bold grey]Closed[/bold grey]"]

app = typer.Typer()

def sort_tickets(ticket: Path):
    for i, status in enumerate(SORT_ORDER):
        status_dir = Path(DEFAULT_FIT_DIR) / status
        if ticket.is_relative_to(status_dir):
            return i

def get_all_tickets_by_status() -> dict[str, list[Path]]:
    tickets_by_status = {k:[] for k in SORT_ORDER}
    for current_path, _, filenames in os.walk(DEFAULT_FIT_DIR):
        current_dir = Path(current_path)
        for status in SORT_ORDER:
            status_dir = Path(DEFAULT_FIT_DIR) / status
            if current_dir.is_relative_to(status_dir):
                for filename in filenames:
                    if filename == ".gitkeep":
                        continue
                    elif filename.endswith(".md"):
                        p = Path(current_path, filename)
                        tickets_by_status[status].append(Path(current_path, filename))

    return tickets_by_status

def get_all_tickets() -> list[Path]:
    """Gets the list of all tickets (in the standard folders), sorted by status and then priority"""
    return [item for sublist in get_all_tickets_by_status().values() for item in sublist]

def find_ticket_file_by_name(name: str, nopartial: bool = False) -> Path | None:
    tickets = get_all_tickets()
    for ticketfile in tickets:
        fuzz_score = fuzz.partial_ratio(ticketfile.name, name) if not nopartial else fuzz.QRatio(ticketfile.name, name)
        if fuzz_score > DEFAULT_FUZZ_THRESHOLD:
            return ticketfile

@app.callback(invoke_without_command=True)
def list_tickets(ctx: typer.Context):
    if not ctx.invoked_subcommand:
        tickets= get_all_tickets_by_status()
        group = Group()
        for i, status in enumerate(SORT_ORDER):
            status_group = Group()
            formatted_status = FORMATTED_SORT_ORDER[i]
            status_group.renderables.append(formatted_status)
            these_tickets = tickets[status]
            if len(these_tickets) > 0:
                for ticket in tickets[status]:
                    status_group.renderables.append(f"    {ticket}")
                    pass
                group.renderables.append(Padding(status_group, 1))
        console = Console()
        console.print(group)
    pass

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

def pprint_ticket(ticketfile: Path, simple: bool = False, expand: bool = False):
    text = ticketfile.read_text()
    if simple:
        print(str(ticketfile))
        print(text)
    else:
        console = Console()
        group = Group()
        post = frontmatter.loads(text)
        if post.content.strip() == "":
            md = "[italic red]File Is Empty[/italic red]"
        else:
            md = Markdown(post.content)
        if post.metadata:
            post.content = ""
            m = Padding(frontmatter.dumps(post).strip("---\n"), 1)
            group.renderables.append(m)
            group.renderables.append(
                Rule("Content"),
            )
        group.renderables.append(md)
        title = str(ticketfile.stem.replace("-", " ").title())
        console.print(Panel(group, title=title, subtitle=str(ticketfile), width=84 if not expand else None))

@app.command()
def show(name: str, nopartial: bool = False, simple: bool = False, expand: bool = False):
    """Prints the targeted ticket. By default prints all pretty with rendered markdown and a border,
    but with --simple just prints the path of the file and its plain text"""
    ticketfile = find_ticket_file_by_name(name, nopartial) 
    if ticketfile:
        pprint_ticket(ticketfile, simple, expand)

@app.command()
def show_current(nopartial: bool = False, simple: bool = False, expand: bool = False):
    """Same as 'show', but prints the current 'in_progress' ticket if 'in_progress' has 
    exactly on ticket."""
    in_progress = get_all_tickets_by_status()["in_progress"]
    if len(in_progress) == 1:
        ticketfile = in_progress[0]
        pprint_ticket(ticketfile, simple, expand)
    else:
        print("in_progress does not have exactly one ticket")

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

@app.command()
def pull():
    """If there are no tickets in in_progress, moves the next
    ticket from "open" into "in_progress" (or from "backlog"
    if no tickets are in "open")"""

    tickets = get_all_tickets_by_status()
    if len(tickets["in_progress"]) == 0:
        if len(tickets["open"]) > 0:
            first = tickets["open"][0]
            first.move(Path(DEFAULT_FIT_DIR) / "in_progress" / first.name)
            print(f"Ticket {first} was moved from 'open' to 'in_progress'")
        elif len(tickets["backlog"]) > 0:
            first = tickets["backlog"][0]
            first.move(Path(DEFAULT_FIT_DIR) / "in_progress" / first.name)
            print(f"Ticket {first} was moved from 'backlog' to 'in_progress'")
    else:
        print("There was a ticket in progress already, so no ticket was moved to 'in_progress'")
        print(f"Current 'in_progress' ticket is {tickets["in_progress"][0]}")

@app.command()
def close(name: str = "", nopartial: bool = False):
    """If no name is provided and there is a ticket in 'in_progress', closes it. Otherwise closes the targeted ticket."""
    ticket: Path | None = None
    if name != "":
        ticket = find_ticket_file_by_name(name, nopartial)
        if not ticket:
            print(f"A ticket matching {name} was not found")
    else:
        tickets = get_all_tickets_by_status()['in_progress']
        if len(tickets) == 1:
            ticket = tickets[0]
        else:
            print("'in_progress' did not have exactly 1 ticket")
    if ticket:
        ticket.move(Path(DEFAULT_FIT_DIR) / "closed" / ticket.name)
        print(f"Closed {ticket}")
    else:
        print("No tickets were closed")
        return False

def main() -> None:
    app()
