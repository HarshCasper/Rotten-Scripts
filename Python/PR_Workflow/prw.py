import click
import requests
from src.extracktor import json_extract
from src.graphqlapi import Queries
from src.prapi import run_query


@click.group()
def main():
    """
    Work with GitHub pull requests.\n
    prw <command> <argument> [options] [flags]
    """


@main.command()
@click.option('-t', '--tag', type=str, help="Search pull request by tag[case sensitive]")
@click.option('-s', '--state', type=click.Choice(['open', 'closed', 'merged']), required=True, help="Show recent merged pull request")
@click.option('-v', '--verbose', is_flag=True, help="enable verbose mode")
@click.option('-p', '--pages', type=int, default=1, help="Show result up to pages")
@click.argument('repos', type=str, required=True)
def repo(repos, state, pages, tag=None, verbose=False, ):
    """This function checks the valid configuration 
    and calls the API on the given repository with arguments and options
    and also prints the output
    """
    if pages > 3:
        click.secho("You can not see more than 3 pages.!", fg='red', bold=True)
        return
    pages = pages*30
    state = state.upper()
    flag = True
    stcolor = {"OPEN": "green", "CLOSED": "red", "MERGED": "yellow"}
    try:
        #read configuration from config.ini file
        with open('config.ini', 'r') as cf:
            token = cf.read()
            if len(token) != 40:
                raise Exception
    except:
        if flag:
            click.secho('Please Verify Your github Token first.!',
                        bold=True, fg='red')
            click.echo('Usage :  auth <token> ')
    else:
        r = repos.split("/")
        if len(r) < 2:
            click.echo(click.secho("SyntaxError:", fg='red', bold=True) +
                       click.echo('invalid syntax for repo : username/repo_name'))
            return
        else:
            result = run_query(
                Queries(f"{r[0]}", f"{r[1]}", state, tag, pages).pulls(), token)
            if verbose:
                print("This feature has not been added yet..comming soon")
            else:

                click.secho(state, fg=stcolor[state], bold=True)
                for i in result['data']['repository']['pullRequests']['nodes']:
                    number = json_extract(i, 'number')
                    title = json_extract(i, 'title')
                    totalCount = json_extract(i, 'totalCount')
                    lname = json_extract(i, 'name')
                    click.secho(
                        f"#{number[0]}  ", fg=stcolor[state], bold=True, nl=False)
                    print(
                        f"Title :{title[0]} ----------> Comments :{totalCount[0]} ---------> labels{lname}")


@main.command()
@click.argument('token')
def auth(token):
    """ Verify Api with GitHub token\n
        example: prw.py auth <token>
    """
    if len(token) == 40:
        with open('config.ini', 'w') as cf:
            cf.write(token)
            click.secho('Verification Successfull 👍', fg='green', bold=True)
    else:
        click.secho('Incorrect token please retry..!', fg='red', bold=True)


def start():
    """
    prw <command> <argument> [options] [flags]
    """

    main(obj={})


if __name__ == '__main__':
    start()
