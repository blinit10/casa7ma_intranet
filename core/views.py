from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.models import InternetNauta, QrData


# Create your views here.
@csrf_exempt
def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # User is active and can log in
            return JsonResponse({'command': "OK", }, status=200)
        else:
            # Invalid username or password
            return JsonResponse({'command': "KO", }, status=403)
    return JsonResponse({'command': "KO", }, status=403)

@csrf_exempt
def get_internet_info(request):
    try:
        internet_nauta = InternetNauta.objects.all()[0]
    except:
        return JsonResponse({'command': "KO"}, status=400)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        internet_nauta.nauta_username = username
        internet_nauta.nauta_password = password
        internet_nauta.save()
    return JsonResponse(
        {'username': internet_nauta.nauta_username, 'autoconnect': 1, 'password': internet_nauta.nauta_password,
         "connected": internet_nauta.connected},status=200)

@csrf_exempt
def internet_nauta_connect(request):
    try:
        internet_nauta = InternetNauta.objects.all()[0]
    except:
        return JsonResponse({'command': "KO"}, status=400)
    if request.method == "POST":
        internet_nauta.connected = False
        internet_nauta.save()
        return JsonResponse({'command': "OK"}, status=200)
    internet_nauta.connected = True
    internet_nauta.save()
    return JsonResponse({'command': "OK"}, status=200)

@csrf_exempt
def get_qr_info(request):
    try:
        qr = QrData.objects.all()[0]
    except:
        return JsonResponse({'command': "KO"}, status=400)
    return JsonResponse(
        {'uri': qr.uri,},status=200)