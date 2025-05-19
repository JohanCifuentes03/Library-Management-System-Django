from datetime import datetime


def greeting(request):
    current_time = datetime.now().time()
    if current_time.hour < 12:
        greeting = "Dias"
    elif current_time.hour < 16:
        greeting = "Tardes"
    else:
        greeting = "Noches"

    return {"greeting": greeting}
