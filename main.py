import requests

usernames = list(map(lambda x: x.strip(), input().split(",")))

session = requests.Session()

for username in usernames:
    tasks = 0
    tasks_names = dict()

    response = session.get('https://codeforces.com/api/user.status?handle={0}&from=1'.format(username))

    if response.json()['status'] == "FAILED":
        print("No such username as {0}".format(username))
        continue

    for result in response.json()['result']:
        competition = result["problem"]["contestId"]
        index = result["problem"]["index"]

        if competition not in tasks_names:
            tasks_names[competition] = []

        if index not in tasks_names[competition]:

            tasks += 1
            tasks_names[competition].append(index)

    print("%s: %d" % (username, tasks))
