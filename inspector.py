import requests


def inspect(url):
    alarms = []
    return alarms


def main():
    urls = ['https://www.impots.gouv.fr/portail/']

    for u in urls:
        alarms = inspect(u)
        if len(alarms) != 0:
            print('Following alarms are raised on website {}'.format(u))
        else:
            print('Website {} was checked OK'.format(u))


main()
