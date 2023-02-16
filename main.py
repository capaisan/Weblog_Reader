import csv
import argparse
import requests
import io
import re

def download_data(url):

    response = requests.get(url)

    return response.text


def image_hits(csv_data, new):
    jpg = 0
    gif = 0
    png = 0

    for row in csv_data:
        zero = row[0]
        if re.search(r'jpg', zero, re.IGNORECASE):
            jpg += 1
        if re.search(r'gif', zero, re.IGNORECASE):
            gif += 1
        if re.search(r'png', zero, re.IGNORECASE):
            png += 1
    total = jpg + gif + png
    percent = (total / new) * 100

    print(f"Image requests account for {percent}% of all requests")

def total(new):
    count = 0
    for i in new:
        count +=1
    return count


def browser_hits(csv_data):
    chrome_num = 0
    fox_num = 0
    saf_num = 0
    ie_num = 0
    for row in csv_data:
        two = row[2]
        if re.search(r'chrome', two, re.IGNORECASE):
            chrome_num += 1
        elif re.search(r'firefox', two, re.IGNORECASE):
            fox_num += 1
        elif re.search(r'safari', two, re.IGNORECASE):
            saf_num += 1
        elif re.search(r'msie', two, re.IGNORECASE):
            ie_num += 1

    browser = {
        'chrome': chrome_num,
        'firefox': fox_num,
        'safari': saf_num,
        'msie': ie_num
    }
    maximum = max(browser, key=browser.get)
    print(f"{maximum.capitalize()} is the most used browser at {browser[maximum]} hits")


def main(url):
    url_data = download_data(url)

    csv_data_image = csv.reader(io.StringIO(url_data))
    csv_data_browser = csv.reader(io.StringIO(url_data))
    new = csv.reader(io.StringIO(url_data))

    amount = total(new)

    image_hits(csv_data_image, amount)
    browser_hits(csv_data_browser)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)