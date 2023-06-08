from django.contrib.auth import login
from django.shortcuts import render , redirect
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random 
import time
import json


from .models import RoomMember
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/frontpage/')
    else:
        form = SignUpForm()

    return render(request, 'base/signup.html', {'form': form})



def getToken(request):
    appId = 'f1ad55fc9cea45a7856250eadf81878b'
    appCertificate = 'be2d095946e043d9851dbf9880031d9e'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230) 
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token,'uid': uid }, safe=False)

def frontpage(request):
    return render(request, 'base/frontpage.html')

def lobby(request):
    return render(request, 'base/lobby.html')


def room(request):
    return render(request, 'base/room.html')

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)

    member, created = RoomMember.objects.get_or_create(
        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )


    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('uid')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid =uid,
        room_name=room_name,

    )

    name = member.name
    return JsonResponse({'name':member.name},safe = False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)

    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],            
        room_name=data['room_name'],
        )
    member.delete()


    return JsonResponse("Member was deleted! ", safe=False)