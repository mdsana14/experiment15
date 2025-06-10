import requests
from django.shortcuts import render

def get_weather(request):
    city = request.GET.get('city', 'Hyderabad')  # Default city
    api_key = 'debe1c45916136b61914e710a92804f0'  # Replace with your OpenWeatherMap API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            context = {'weather': data, 'city': city}
        else:
            context = {'error': data.get("message", "City not found."), 'city': city}
    except Exception as e:
        context = {'error': str(e), 'city': city}

    return render(request, 'weatherapp/weather_minimal.html', context)
