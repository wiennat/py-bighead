import sys

def main():
    url = sys.argv[1]
    header_size = sys.argv[2]
    body_size = sys.argv[3]

    cookies = dict(cookies='a' * header_size)
    data = {"key": 'b'*  body_size }
    try:
        print("send ing request with following configuration")
        print("url - %s" % url)
        print("header size - %s" % len(header_size)
        print("cookies store- %s" % len(body_size))
        r = requests.post(url, data=data, cookies=cookies)
    except:
        print("error"


if __name__ == "__main__":
    main()
