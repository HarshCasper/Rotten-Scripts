import github
import pickledb
import json
import argparse
import sys

# Collect Information for Databse
def collect(user, repo, token, org):
    if org is None:
        org = user

    db = __load_db(repo=repo)

    # Connect API using PAT
    gh = github.GitHub(access_token=token)
    try:
        gh.repos(org, repo).get()
    except Exception:
        sys.exit('No Data')

    if user is not None and org != user:
        try:
            gh.repos(org, repo).collaborators(user).get()
        except Exception:
            sys.exit('No Data')

    views_data = gh.repos(org, repo).traffic.views.get()
    found_new_data = False
    for view_per_day in views_data['views']:
        timestamp = view_per_day['timestamp']
        data = {'uniques': view_per_day['uniques'], 'count': view_per_day['count']}
        if db.get(timestamp) is None or db.get(timestamp) is False:
            db.set(timestamp, json.dumps(data))
            print(timestamp, data)
            found_new_data = True
        else:
            db_data = json.loads(db.get(timestamp))
            if db_data['uniques'] < data['uniques']:
                db.set(timestamp, json.dumps(data))
                print(timestamp, data)
                found_new_data = True
    if not found_new_data:
        print('No Data')
    db.dump()


def view(repo):
    db = __load_db(repo=repo)
    timestamps = db.getall()
    for ts in sorted(timestamps):
        print(ts, db.get(ts))
    print(len(timestamps), 'elements')


def __load_db(repo):
    return pickledb.load('{repo}_views.db'.format(repo=repo), False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['collect', 'view'])
    parser.add_argument('-u', '--github_user', action='store')
    parser.add_argument('-t', '--github_access_token', action='store')
    parser.add_argument('-o', '--github_org', action='store')
    parser.add_argument('-r', '--github_repo', action='store')
    parser.add_argument('-v', '--view', help='view DB content', action='store_true')

    args = parser.parse_args()

    if args.action == 'view':
        if args.github_repo is None:
            sys.exit('You need to provide GitHub repo: -r|--github_repo')
        view(repo=args.github_repo)
    else:
        if (args.github_repo is None or
           args.github_access_token is None or
           (args.github_user is None and args.github_org is None)):
            sys.exit('Recheck all the arguments, view README\n')
        collect(user=args.github_user, repo=args.github_repo, token=args.github_access_token, org=args.github_org)


if __name__ == "__main__":
    main()