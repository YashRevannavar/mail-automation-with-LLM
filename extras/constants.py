import os
from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

load_dotenv()

## Loading Environment Variables
MISTRIAL_API_KEY = os.environ['MISTRIAL_API_KEY']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_SENDER = os.environ['EMAIL_SENDER']


## LLM and AI

subject_parser = ResponseSchema(name="Subject",
                                description="The subject of the email",
                                type="string")
body_parser = ResponseSchema(name="Body",
                             description="The body of the email",
                             type="string")


response_schema = [subject_parser, body_parser]
parser = StructuredOutputParser.from_response_schemas(response_schema)

prompt = """
Write a mail to .......{{Your details here, Tip be as specific & descriptive as you can}}.......

Here are my details(use this details only for the email signature):
Name: Your Name
Email: Your Email
phone: Your Phone Number

Include my signature at the end of the email with above details.
refer this example but do not replicate the same  = [
{{Your example email here.}}
]

{email}
{format_instructions}
"""
