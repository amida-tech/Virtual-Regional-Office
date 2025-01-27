from jinja2 import Environment, PackageLoader, select_autoescape
from pathlib import Path
import json
import os
import pdfkit

lib_dir = os.path.dirname(__file__)
WKHTMLTOPDF_PATH = Path(os.environ["WKHTMLTOPDF_PATH"]).resolve()


def get_template(template_name: str) -> str:
    available_templates = {
        "hypertension": "hypertension",
        "cancer": "pact_data_sheet"
    }

    selected_template = available_templates[template_name]

    return selected_template



def generate_template_file(template_name: str, pdf_data) -> str:
    jinja_env = Environment(
        loader=PackageLoader("lib"),
        autoescape=select_autoescape()
    )

    template_file = get_template(template_name)
    placeholder_variables = json.load(open(os.path.join(lib_dir, f"pdf_variables/{template_file}.json")))
    filled_variables = {key: pdf_data.get(key, placeholder_variables[key]) for key in placeholder_variables}
    template = jinja_env.get_template(os.path.join(lib_dir, f"pdf_templates/{template_file}.html"))
    generated_html = template.render(**filled_variables)
    
    return generated_html


def generate_pdf_from_string(html: str) -> bytes:
    assert WKHTMLTOPDF_PATH.exists()
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

    options = {
        "dpi": 300,
        "page-size": "Letter",
        "margin-top": "0.25in",
        "margin-right": "0.25in",
        "margin-bottom": "0.25in",
        "margin-left": "0.25in",
        "encoding": "UTF-8",
        "zoom": "0.8"
    }

    return pdfkit.from_string(html, False, options=options, configuration=config)
