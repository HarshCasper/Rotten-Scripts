import datetime
import math
import click
from rich import print as rprint
from src.extracktor import json_extract


def truncate(string, width):
    """this function use to truncate the string up to given width"""
    if len(string) > width:
        string = string[: width - 3] + "..."
    return string


def prdate(crdate, enddate):
    """
    this function returns pull request duration
    """
    if not enddate[0]:
        end_dates = datetime.datetime.now().replace(microsecond=0)
    else:
        end_dates = datetime.datetime.strptime(enddate[0], "%Y-%m-%dT%H:%M:%SZ")
    create_dates = datetime.datetime.strptime(crdate[0], "%Y-%m-%dT%H:%M:%SZ")
    return str(end_dates - create_dates)


def print_output(result, verbose, state, col):
    """
    this function use to formate the output according to terminal size
    col - > column
    """
    state_color = {"OPEN": "green", "CLOSED": "red", "MERGED": "yellow"}
    if verbose:
        click.secho(state, fg=state_color[state], bold=True)
        click.secho("Verbose mode", fg="red", bold=True)
        print("\n")
        for i in result["data"]["repository"]["pullRequests"]["nodes"]:
            number = json_extract(i, "number")
            title = truncate(json_extract(i, "title")[0], math.ceil(col / 5))
            # totalCount = json_extract(i, 'totalCount')
            create_date = json_extract(i, "createdAt")
            closed_date = json_extract(i, "closedAt")
            dates = prdate(create_date, closed_date)
            lname = truncate(", ".join(json_extract(i, "name")), math.ceil(col / 5))
            rprint(
                f"[bold {state_color[state]}]#{number[0]}[/bold {state_color[state]}]",
                title.ljust(math.ceil(col / 4)),
                f"( {lname} )".ljust(math.ceil(col / 4)),
                dates,
            )
    else:
        click.secho(state, fg=state_color[state], bold=True)
        print("\n")
        for i in result["data"]["repository"]["pullRequests"]["nodes"]:
            number = json_extract(i, "number")
            title = truncate(json_extract(i, "title")[0], math.ceil(col / 3))
            rprint(
                f"[bold {state_color[state]}]#{number[0]}[/bold {state_color[state]}]",
                title.ljust(math.ceil(col / 4)),
            )
