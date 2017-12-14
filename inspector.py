import requests


def inspect(url):
    alarms = []

    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        alarms.append('HTTP request error {}'.format(r.status_code))
    return alarms


def get_urls():
    urls = []
    try:
        urls_file = open('urls.txt', 'r')
        for line in urls_file:
            line = line.strip()
            if len(line):
                urls.append(line)

    except FileNotFoundError as e:
        print(e)

    return urls


def main():
    urls = get_urls()
    print(urls)

    for u in urls:
        alarms = inspect(u)
        if len(alarms) != 0:
            print('Following alarms are raised on website {}:'.format(u))
            for a in alarms:
                print('* {}'.format(a))
        else:
            print('Website {} was checked OK'.format(u))


main()
