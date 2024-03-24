from langchain_mistralai.chat_models import ChatMistralAI
from langchain.prompts import PromptTemplate
from extras.constants import *


def email_llm_model():
    """
    This function created a mail to BerlinNova company which is a real estate company.
    :return:
    """
    prompt_template= PromptTemplate(
        template=prompt,
        input_variables=["email"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
        format_instructions=parser.get_format_instructions()
    )
    llm = ChatMistralAI(mistral_api_key=MISTRIAL_API_KEY, temperature=0.9, model='mistral-small')
    response = llm.invoke(str(prompt_template))
    response_as_dict = parser.parse(response.content)
    return response_as_dict

