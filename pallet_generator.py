import re
from typing import List

from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import (
    PromptTemplate,
)
from langchain.schema import PromptValue

from models import ColorPallet, FreeformColorPallet
from utils import debug_log

pattern = re.compile(r'^[a-zA-Z\s]+$')

base_prompt = """
Generate colors for
accent color of the theme,
text on the page,
background of page,
primary color of buttons,
secondary color of buttons, 

All color codes should be different.
There should be some core colors that are used on the website, and some accent colors that are used for buttons and other elements.
Color are going to be used on a website where the theme can be defined"""

keyword_prompt = f"""
{base_prompt} using the following keywords:
{{keywords}}

{{format_instructions}}
"""

sentence_prompt = f"""
{base_prompt}  by:
{{sentence}}

{{format_instructions}}
"""

freeform_prompt = f"""
Generate {{num_colors}} colors. These color codes are going to be used on a website.
All color codes should be different. Arange colors in a way that similar colors are together.
There should be some core colors that are used on the website, and some accent colors that are used for buttons and other elements.
Color are going to be used on a website where the theme can be defined
"""

freeform_keyword_prompt = f"""
{freeform_prompt} using the following keywords:
{{keywords}}

{{format_instructions}}
"""

freeform_sentence_prompt = f"""
{freeform_prompt}  by:
{{sentence}}

{{format_instructions}}
"""


def _filter_keywords(keywords: List[str]) -> List[str]:
    return [keyword for keyword in keywords if pattern.match(keyword.strip())]


class PalletGenerator:
    def __init__(self, model_name: str, temperature: float = 0.0):
        self.model_name = model_name
        self.temperature = temperature
        self.model = OpenAI(model_name=self.model_name, temperature=self.temperature)

    def _generate_pallet(self, input: PromptValue) -> str:
        model_input = input.to_string()
        debug_log(f"model_input: {model_input}")

        model_output = self.model(model_input)
        debug_log(f"model_output: {model_output}")
        return model_output

    def generate_pallet_using_keywords(self, keywords: List[str]):
        pallet_parser = PydanticOutputParser(pydantic_object=ColorPallet)
        keyword_prompt_template = PromptTemplate(
            template=keyword_prompt,
            input_variables=["keywords"],
            partial_variables={"format_instructions": pallet_parser.get_format_instructions()},
        )
        model_input = keyword_prompt_template.format_prompt(keywords=", ".join(_filter_keywords(keywords)))
        model_output = self._generate_pallet(model_input)
        return pallet_parser.parse(model_output)

    def generate_pallet_using_text(self, sentence: str):
        sentence = sentence[:200]
        pallet_parser = PydanticOutputParser(pydantic_object=ColorPallet)
        sentence_prompt_template = PromptTemplate(
            template=sentence_prompt,
            input_variables=["sentence"],
            partial_variables={"format_instructions": pallet_parser.get_format_instructions()},
        )
        model_input = sentence_prompt_template.format_prompt(sentence=sentence)
        model_output = self._generate_pallet(model_input)
        return pallet_parser.parse(model_output)

    def generate_freeform_pallet_using_keywords(self, keywords: List[str], num_colors: int = 5):
        pallet_parser = PydanticOutputParser(pydantic_object=FreeformColorPallet)
        keyword_prompt_template = PromptTemplate(
            template=freeform_keyword_prompt,
            input_variables=["keywords", "num_colors"],
            partial_variables={"format_instructions": pallet_parser.get_format_instructions()},
        )
        model_input = keyword_prompt_template.format_prompt(
            keywords=", ".join(_filter_keywords(keywords)),
            num_colors=num_colors
        )
        model_output = self._generate_pallet(model_input)
        return pallet_parser.parse(model_output)
