import os
import click
from src.drivefunc import print_output
from src.graphqlapi import Queries
from src.prapi import run_query


@click.group()
def main():
    """
    Work with GitHub pull requests.\n
    prw <command> <argument> [options] [flags]
    """


@main.command()
@click.option(
    "-t", "--tag", type=str, help="Search pull request by tag[case sensitive]"
)
@click.option(
    "-s",
    "--state",
    type=click.Choice(["open", "closed", "merged"]),
    required=True,
    help="Show recent merged pull request",
)
@click.option("-v", "--verbose", is_flag=True, help="enable verbose mode")
@click.option("-p", "--pages", type=int, default=1, help="Show result up to pages")
@click.argument("repos", type=str, required=True)
def repo(
    repos,
    state,
    pages,
    tag=None,
    verbose=False,
):
    """This function checks the valid configuration
    and calls the API on the given repository with arguments and options
    and also prints the output
    """
    if pages > 3:
        click.secho("You can not see more than 3 pages.!", fg="red", bold=True)
        return
    pages = pages * 30
    state = state.upper()
    flag = True
    try:
        # read configuration from config.ini file
        with open("config.ini", "r") as conf:
            token = conf.read()
            if len(token) != 40:
                raise FileNotFoundError
    except:
        if flag:
            click.secho("Please Verify Your github Token first.!", bold=True, fg="red")
            click.echo("Usage :  auth <token> ")
    else:
        repo_n = repos.split("/")
        if len(repo_n) < 2:
            click.echo(
                click.secho("SyntaxError:", fg="red", bold=True)
                + click.echo("invalid syntax for repo : username/repo_name")
            )
        else:
            col = int(list(os.get_terminal_size())[0])
            result = run_query(
                Queries(f"{repo_n[0]}", f"{repo_n[1]}", state, tag, pages).pulls(),
                token,
            )
            print_output(result, verbose, state, col)


@main.command()
@click.argument("token")
def auth(token):
    """Verify Api with GitHub token\n
    example: prw.py auth <token>
    """
    if len(token) == 40:
        with open("config.ini", "w") as conf:
            conf.write(token)
            click.secho("Verification Successfull 👍", fg="green", bold=True)
    else:
        click.secho("Incorrect token please retry..!", fg="red", bold=True)


def start():
    """
    prw <command> <argument> [options] [flags]
    """

    main()


if __name__ == "__main__":
    start()
