import os
import csv
import click
import requests


def run_query(token, repo):
    """A simple function to use requests.post to make the API call. Note the json= section."""
    repo = repo.split("/")
    name = repo[1]
    owner = repo[0]
    query = query_string(name, owner)
    headers = {"Authorization": f"token {token}"}
    res = requests.post(
        "https://api.github.com/graphql", json={"query": query}, headers=headers
    )
    if res.status_code == 200:
        return res.json()
    raise Exception(
        "Query failed to run by returning code of {}".format(res.status_code)
    )


def query_string(name, owner):
    """it built query string on given name of repo and owner of repo"""
    query = """
    {
    	repository(name: "%s", owner: "%s") {
    		ref(qualifiedName: "master") {
    			target {
    				... on Commit {
    					id
    					history {
    						pageInfo {
    							hasNextPage
    						}
    						edges {
    							node {
    								author {
    									name
    									email
    									user {
    										name
    									}
    								}
    							}
    						}
    					}
    				}
    			}
    		}
    	}
    }
    """ % (
        name,
        owner,
    )
    return query


@click.command()
@click.argument("token", required=True, type=str)
@click.argument("repo", required=True, type=str)
def main(token, repo):
    """
    This function takes token and repository name as input and fetch email,
    name and username and store them in csv file \n
    usage:
    python email_scrap.py <token> <repo_name>
    """
    with open("commits_email.csv", "w") as new_file:
        fieldnames = ["Name", "Username", "Email"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
        csv_writer.writeheader()
        result = run_query(token, repo)
        unique_user_name = set()
        for i in result["data"]["repository"]["ref"]["target"]["history"]["edges"]:
            email = i["node"]["author"]["email"].split("+")[-1]
            user_name = i["node"]["author"]["name"]
            name = i["node"]["author"]["user"]["name"]
            if user_name not in unique_user_name:
                csv_writer.writerow(
                    {"Name": f"{name}", "Username": f"{user_name}", "Email": f"{email}"}
                )
                unique_user_name.add(user_name)
    click.secho(
        "\n-> 👍 Successfully Saved at " + f"{os.path.abspath(os.getcwd())}",
        fg="green",
        bold=True,
    )


if __name__ == "__main__":
    main()
