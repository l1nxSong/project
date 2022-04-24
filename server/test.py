import requests


class Test(object):
    def __init__(self, url, vul_to_check):
        self.url = url
        self.vul_to_check = vul_to_check
        self.check(url, vul_to_check)
        # self.isValid = url_test(url)

    def url_test(self, url):
        # check if this is a valid url
        try:
            # try to send GET request to the server
            req = requests.get(url, timeout=10)
            if req.status_code != 200:
                return False
            else:
                return True

        except Exception as e:
            return False

    def check(self, url, vul_to_check):
        filename = vul_to_check + '.txt'
        payload = []
        # open corresponding file according to the name
        with open(filename, 'r', encoding='utf-8') as f:
            for i in f:
                # add the payloads in the file to the list line by line
                payload.append(i.strip())

        # start to check
        # first split the url by ? to get the route
        domain = url.split("?")[0]
        for _payload in payload:
            # combine the route with the payload to test
            new_url = domain + _payload
            result = self.url_test(new_url)
            if result == True:
                print("XSS FOUND: " + new_url)
            else:
                print("Pass: " + new_url)

