import re

# re.sub => useful to filter data
# re.search

url = input("url twitter: ").strip()
username = re.sub(r"^(https?://)?(www.\.)?twitter\.com/", "", url)

print(f"Username : {username}")


if matches := re.search(r"^https?://(www\.)?twitter\.(.+)/(\w)$", url.re.IGNORECASE):
    print(f"Username: {matches.group(3)}")
