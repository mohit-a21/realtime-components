from generate_colors import generate_color_boxes, generate_freeform_color_boxes
from pallet_generator import PalletGenerator
from utils import pretty_log

pallet_generator = PalletGenerator(model_name="text-davinci-003", temperature=0.8)


def cli_keywords():
    while True:
        query = input("\nEnter comma separated keywords: ")
        keywords = query.split(",")
        generated_pallet = pallet_generator.generate_pallet_using_keywords(keywords)
        pretty_log("🦜 Generated  🦜")
        print(generated_pallet)
        generate_color_boxes(generated_pallet)


def cli_freeform_keywords():
    while True:
        query = input("\nEnter comma separated keywords: ")
        keywords = query.split(",")
        generated_pallet = pallet_generator.generate_freeform_pallet_using_keywords(keywords)
        pretty_log("🦜 Generated  🦜")
        print(generated_pallet)
        generate_freeform_color_boxes(generated_pallet)


def cli_sentence():
    while True:
        sentence = input("\nEnter a sentence: ")
        generated_pallet = pallet_generator.generate_pallet_using_text(sentence)
        pretty_log("🦜 Generated  🦜")
        print(generated_pallet)
        generate_color_boxes(generated_pallet)


if __name__ == '__main__':
    cli_freeform_keywords()
