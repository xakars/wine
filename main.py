import datetime
import pandas
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def validate(year: int):
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


def get_wines_from_exel():
    excel_data_df = pandas.read_excel(
        'wine3.xlsx',
        names=['category','title','variety','price','image', 'promo'],
        keep_default_na=False)
    table = excel_data_df.to_dict(orient='records')
    wines = defaultdict(list)
    for line in table:
        wines[line['category']].append(line)
    return wines


def get_together_year():
    founded_year = 1920
    current_year = datetime.datetime.now().year
    return current_year-founded_year


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
rendered_page = template.render(
    year=get_together_year(),
    ending=validate(get_together_year()),
    wines=get_wines_from_exel())

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
