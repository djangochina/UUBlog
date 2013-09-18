from django.http import HttpResponse
import django.dispatch
from django.views.decorators.csrf import csrf_exempt

def upload_received_handler(sender, data, **kwargs):

     if file:

          # process the received file here

          print data.file
          
upload_received = upload_received_handler;

@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'])
    return HttpResponse('True')
