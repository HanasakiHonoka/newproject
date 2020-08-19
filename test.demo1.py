import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    s = """
    github.com
    assets-cdn.github.com
    avatars0.githubusercontent.com
    avatars1.githubusercontent.com
    documentcloud.github.com 
    help.github.com
    nodeload.github.com
    raw.github.com
    status.github.com
    training.github.com
    github.io
    """
    import requests
    from bs4 import BeautifulSoup

    ans = []
    for i in s.split():
        url = "http://ip.chinaz.com/" + i.strip()
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text)
        x = soup.find(class_="IcpMain02")
        x = x.find_all("span", class_="Whwtdhalf")
        x = "%s %s" % (x[5].string.strip(), i.strip())
        print(x)
        ans.append(x)

    hosts = r"C:\Windows\System32\drivers\etc\hosts"
    with open(hosts, "r") as f:
        content = [i for i in f.readlines() if i.startswith("#")]
        content.extend(ans)
    with open(hosts, "w") as f:
        f.write("\n".join(content))
    pass