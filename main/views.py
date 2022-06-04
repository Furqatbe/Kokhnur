from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def Index(request):
    title = Title.objects.last()
    service = Service.objects.all().order_by('-id')[0:3]
    service2 = Service2.objects.last()
    service3 = Service3.objects.last()
    features = Features.objects.last()
    features1 = Features1.objects.last()
    narxlar = Narxlar.objects.last()
    narxlar2 = Narxlar2.objects.last()
    narxlar33 = Narxlar33.objects.last()
    video = YouTubeVideo.objects.last()
    team = Team.objects.last()
    jamoa = Jamoa.objects.last()
    contact = Contact.objects.last()
    
    
    context = {
        'title':title,
        'service':service,
        'service2':service2,
        'service3':service3,
        'features':features,
        'features1':features1,
        'narxlar':narxlar,
        'narxlar2':narxlar2,
        'narxlar33':narxlar33,
        'video':video,
        'team':team,
        'jamoa':jamoa,
        'contact':contact
        
    }
    return render(request, 'index.html', context)

def AddContact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email = request.POST.get('email')
        phone =request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
       

        Contact1.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
    return redirect('index')