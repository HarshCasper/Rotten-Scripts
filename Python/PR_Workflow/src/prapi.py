import requests


def run_query(query, token):
    """A simple function to use requests.post to make the API call. Note the json= section."""

    headers = {"Authorization": f"token {token}"}
    res = requests.post(
        "https://api.github.com/graphql", json={"query": query}, headers=headers
    )
    if res.status_code == 200:
        return res.json()
    raise Exception(
        "Query failed to run by returning code of {}. {}".format(
            res.status_code, query
        )
    )
