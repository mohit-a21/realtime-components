from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pydantic import BaseModel, Field

from models import ColorPallet, FreeformColorPallet
from pallet_generator import PalletGenerator


# Define the request model using Pydantic
class KeywordsRequest(BaseModel):
    keywords: list[str]
    count: int = Field(default=5)


class TextRequest(BaseModel):
    text: str
    count: int = Field(default=5)


pallet_generator = PalletGenerator(model_name="text-davinci-003", temperature=0.8)


@csrf_exempt
def generate_palette_keywords(request):
    try:
        body = request.body
        keywords_request = KeywordsRequest.parse_raw(body)

        # Get the list of keywords
        keywords = keywords_request.keywords

        # Generate the color palette (replace this with your actual logic)
        generated_pallet: ColorPallet = pallet_generator.generate_pallet_using_keywords(keywords)

        # Return the color palette
        return JsonResponse(data=generated_pallet.dict())

    except Exception as e:
        return JsonResponse(data={'error': str(e)}, status=400)


@csrf_exempt
def generate_palette_text(request):
    try:
        # Validate the request payload
        body = request.body
        text_request = TextRequest.parse_raw(body)

        # Get the list of keywords
        text = text_request.text

        # Generate the color palette (replace this with your actual logic)
        generated_pallet: ColorPallet = pallet_generator.generate_pallet_using_text(text)

        # Return the color palette
        return JsonResponse(data=generated_pallet.dict())

    except Exception as e:
        return JsonResponse(data={'error': str(e)}, status=400)


@csrf_exempt
def generate_freeform_palette_keywords(request):
    try:
        # Validate the request payload
        body = request.body
        keywords_request = KeywordsRequest.parse_raw(body)

        # Get the list of keywords
        keywords = keywords_request.keywords
        count = keywords_request.count

        # Generate the color palette (replace this with your actual logic)
        generated_pallet: FreeformColorPallet = pallet_generator.generate_freeform_pallet_using_keywords(keywords,
                                                                                                         count)

        # Return the color palette
        return JsonResponse(data=generated_pallet.dict())

    except Exception as e:
        return JsonResponse(data={'error': str(e)}, status=400)


@csrf_exempt
def index(request):
    return JsonResponse(data={'msg': 'success'})
