import requests

usernames = list(map(lambda x: x.strip(), input().split(",")))

session = requests.Session()

for username in usernames:
    tasks_completed = 0
    completed_tasks_names = dict()

    response = session.get('https://codeforces.com/api/user.status?handle={0}&from=1'.format(username))

    if response.json()['status'] == "FAILED":
        print("No such username as {0}".format(username))
        continue

    for result in response.json()['result']:
        competition = result["problem"]["contestId"]
        index = result["problem"]["index"]

        if competition not in completed_tasks_names:
            completed_tasks_names[competition] = []

        if result['verdict'] == "OK" and index not in completed_tasks_names[competition]:

            tasks_completed += 1
            completed_tasks_names[competition].append(index)

    print("%s: %d" % (username, tasks_completed))
