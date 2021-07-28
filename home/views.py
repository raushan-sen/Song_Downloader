from os import link
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse, request
from home.models import *
from static.scripts.youtube import *
import string
import random

def aslink(tag):
    head=tag.split('-')
    if len(head)==2:
        cap1=head[0].capitalize()
        cap2=head[1].capitalize()
        combine=[cap1,cap2]
        cc=' '.join(combine)
    else:
        cc=head[0].capitalize()
    return cc


# size=8
# chars=string.ascii_uppercase + string.digits
# b=''.join(random.choice(chars) for _ in range(size))

popular_posts=Song.objects.filter().order_by('-View')

def find(num,argsss):
    result=argsss.objects.all()[:int(num)]    
    return result


def postcategery(num,label):
    post=Song.objects.filter(Genere__CategeryName=str(label))[:int(num)]
    return post



def home(request):
    # setup=Setup.objects.all()[0]
    context={
        'popular_posts':popular_posts[:4],
        'latest_posts':find(4,Song),
        'genere':find(6,Genere),
        'gener':find(4,Genere),
        'sing':find(7, Singer),
        # 'setup':setup,
        'hindi_posts':postcategery(4,'Hindi Song'),
        'English_posts':postcategery(4,'English Songs'),
    }
    return render(request, 'home.html',context)


def post(request,slug):
    post=Song.objects.filter(Slug=str(slug))

    if post.count() == 0:
        context={
            'type':'Url',
            'url':slug,
            'sing':find(7, Singer),
            
        }
        return render(request, '404.html',context)
    
    else:

        mainpost=post[0]
        postf=Song.objects.filter(Slug=slug)[0]
        postf.View=postf.View+1
        postf.save()
        singe=mainpost.singerName.all()
        
        if singe.count()==0:
            result=singe[0]
        else:
            resultf=[res.Name for res in singe]

            result=','.join(resultf)


        audio_url=youtube(mainpost.YoutubeId,None)
        context={
            'popular_posts':popular_posts[:4],
            'latests':find(4,Song),
            'gener':find(4,Genere),
            'post':mainpost,
            'sing':find(7, Singer),
            'singers':result,
            'audio_url':audio_url,
        }

        return render(request, 'page.html',context)

    
def label(request,slug):
    post=Genere.objects.filter(Slug=slug)[0]
    p=Song.objects.filter(Genere__Slug=slug)[:4]
        
    context={
        'labex':f"<a href='/'>Home</a> > <a href='/tag/{ slug }'>{post.CategeryName}</a>",
        'label':post.CategeryName,
        'posts':p,
        'sing':find(7, Singer),
    }

    return render(request,'label.html',context)

def search(request):
    searc=request.GET.get('q')
    posts=Song.objects.filter(SongName__contains=str(searc))
    postlen=len(posts)
    context={
        'labex':f"'{searc}' Releated Search Results :",
        'label':searc,
        'postlength':postlen,
        # 'leng':leng,
        'posts':posts,
        'sing':find(7,Singer),
    }
    return render(request,'label.html',context)


def singer(request,singer):
    # print(singer)
    singers=Singer.objects.distinct()
    try:
        for sin in singers:
            if sin.Name==singer:
                ff=Song.objects.filter(singerName__id=sin.pk)
        

        context={
            'posts':ff,
            'label':singer,
            'labex':f"Singer ' {singer} ' Releated Songs:",
            'sing':find(7,Singer),
        }
        return render(request,'label.html',context)
    except:
        context={
            'type':'Url',
            'url':os.path.join(BASE_DIR,'static'),
            'sing':find(7,Singer),
        }
        return render(request,'404.html',context)



def ggg(request):
    if request.method == 'POST':
        s=request.POST['dd']
        return HttpResponse(s)
    else:
        s=None
        return render(request,"try.html",{'s':s})


def download(request):
    if request.method == 'POST':
        name=request.POST['class']
        idxx=request.POST['id']
        print(name+idxx)
        return JsonResponse({"name":name,
        "idx":idxx})

def seeall(request,categery):
    return render(request,'label.html')
    