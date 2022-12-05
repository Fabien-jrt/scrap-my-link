import argparse
import requests
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(
                    prog = "ScrapMyLink",
                    description = "Gather all the links in the given webpage")
    parser.add_argument("url", help="the http link to scrap from")
    parser.add_argument("--format", choices=["text", "csv", "pdf"], help="format the output to the given format [default: text]")
    args = parser.parse_args()

    url = args.url
    try:
        html_text = requests.get(url).text
    except:
        print(f'Invalid URL: "{url}"')
        exit(0)

    soup = BeautifulSoup(html_text, "html.parser")

    if args.format == "pdf":
        print("pdf export")
    elif args.format == "csv":
        print("source,link")
        for link in soup.find_all("a"):
            print(f'"{url}"', end=",")
            print('"', link.get("href"), '"', sep="")
    else:
        for link in soup.find_all("a"):
            print(link.get("href"))
main()

