import datetime
import os
from dotenv import load_dotenv
import pandas
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_ending_for_year(year: int):
    rule = {
        "1": "год",
        "2": "года",
        "3": "лет"
    }
    end = year % 100
    if 5 <= end <= 20:
        return rule.get("3")
    end = year % 10
    if end == 1:
        return rule.get("1")
    elif end in (2,3,4):
        return  rule.get("2")
    else:
        return rule.get("3")


def get_wines_from_exel(path: str) -> dict:
    excel_data_df = pandas.read_excel(
        path,
        names=['category','title','variety','price','image', 'promo'],
        keep_default_na=False)
    wines_from_exel = excel_data_df.to_dict(orient='records')
    wines = defaultdict(list)
    for wine in wines_from_exel:
        wines[wine['category']].append(wine)
    return wines


def get_winery_age() -> int:
    founded_year = 1920
    current_year = datetime.datetime.now().year
    return current_year-founded_year


def start_server(year: int, ending: str, wines: dict) -> None:
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        year=year,
        ending=ending,
        wines=wines)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


def main():
    load_dotenv()
    path = os.environ["PATH_TO_EXEL_FILE"]
    wines = get_wines_from_exel(path)
    age = get_winery_age()
    ending = get_ending_for_year(age)
    start_server(age, ending, wines)


if __name__ == '__main__':
    main()