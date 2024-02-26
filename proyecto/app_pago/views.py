from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import mercadopago


def pagar(request):
    if request.method == 'POST':
        mp = mercadopago.MP(settings.MERCADOPAGO_CLIENT_ID, settings.MERCADOPAGO_CLIENT_SECRET)
        preference_data = {
            "items": [
                {
                    "title": "Producto",
                    "quantity": 1,
                    "currency_id": "PEN",  # Soles peruanos
                    "unit_price": 100,     # Precio del producto
                }
            ]
        }
        preference = mp.create_preference(preference_data)
        print(preference)
        return JsonResponse(preference)
    return render(request, 'pagar.html')
