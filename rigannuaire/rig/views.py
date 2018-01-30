from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
#import coreapi
import sys
import math
sys.path.append(".")
import urllib3
import json
from io import StringIO
from . import Perso as vh

def index(request):
    template = loader.get_template('rig/index.html')
    return HttpResponse(template.render(request=request))
# Create your views here.

def ids(request,ids):
    context = {
        'talk': [],
    }
    http = urllib3.PoolManager()
    fields={'aa':{'id': ids}}
    encoded_data = json.dumps(fields).encode('utf-8')
    r = http.request(
        'POST',
        'http://annuaire.gopiko.fr/search',
        body=encoded_data,
        headers={'Content-Type': 'application/json'}
    )
    io = StringIO(r.data.decode("utf-8") )
    bb = json.load(io)
    context["talk"] = bb
    print(context["talk"])
    return render(request, 'rig/id.html', context)
    

def search(request):
    form = ContactForm()
    context = {
        'form': form,
        'talk': [],
        'how': 0
    }
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            http = urllib3.PoolManager()
            email = request.POST.get('email')
            lname = request.POST.get('lname')
            fname = request.POST.get('fname')
            snbr = request.POST.get('snbr')
            sn = request.POST.get('sn')
            st = request.POST.get('st')
            city = request.POST.get('city')
            sigle = request.POST.get('sigle')
            zips = request.POST.get('zips')
            tel = request.POST.get('tel')
            gender = request.POST.get('gender')
            fields={'aa':{'fname': fname,'lname' : lname,'email': email,'nbrs': snbr,'ns':sn,'ts':st,'nc':city,'cpc':sigle,'nbrc':zips,'tel':tel,'gender':gender}}
            encoded_data = json.dumps(fields).encode('utf-8')
            r = http.request(
                'POST',
                'http://annuaire.gopiko.fr/search',
                body=encoded_data,
                headers={'Content-Type': 'application/json'}
            )
            io = StringIO(r.data.decode("utf-8") )
            bb = json.load(io)
            if bb:
                for cc in bb:
                    context['talk'].append(cc)
                context['how']= math.ceil(len(context['talk'])/10)
                print(context['how'])
        template = loader.get_template('rig/searchers.html')
        return render(request, 'rig/searchers.html', context)
    
    template = loader.get_template('rig/searcher.html')
    return render(request, 'rig/searcher.html', context)
    
def annuaire(request):
    template = loader.get_template('rig/annuaire.html')
    return HttpResponse(template.render(request=request))
    


def whatis(odn):
    a = ""
    if (odn == "fn" or odn == "ln"):
        return ["http://schema.org/person","name"]
    if (odn == "city" or odn == "street" or odn == "zip" or odn == "sigle"):
        if (odn == "city" or odn == "sigle"):
            return ["http://schema.org/adress","city"]
        if (odn == "street"):
            return ["http://schema.org/adress","street"]
        if (odn == "zip"):
            return ["http://schema.org/adress","zip"]
    if (odn == "email" or odn == "tel"):
        return ["http://schema.org/person","contact"]
    return ""
    
def annuaires(request,odn):
    context = {
        'talk': [],
        'lol': [],
        'ff': odn,
    }     
    http = urllib3.PoolManager()
    r = http.request(
        'POST',
        'http://annuaire.gopiko.fr/query/'+odn,
        headers={'Content-Type': 'application/json'}
    )
    io = StringIO(r.data.decode("utf-8") )
    bb = json.load(io)
    context["talk"] = bb
    context["lol"] = whatis(odn)
    template = loader.get_template('rig/annuaires.html')
    return render(request, 'rig/annuaires.html', context)

def fu(a):
    b = {'fn': 'fname','ln' : 'lname','email': 'email','street':'sn','city':'city','sigle':'cpc','zip':'zip','tel':'tel'}
    if a in b:
        return b[a]
    return false
def anu(request,odn,idn):
    b = fu(odn)
    context = {
        'talk': [],
    }
    
    if (b != False):
        fields={'aa':{b:idn}}
        http = urllib3.PoolManager()
        encoded_data = json.dumps(fields).encode('utf-8')
        r = http.request(
            'POST',
            'http://annuaire.gopiko.fr/search',
            body=encoded_data,
            headers={'Content-Type': 'application/json'}
        )
        io = StringIO(r.data.decode("utf-8") )
        bb = json.load(io)
        context['talk']=bb
        print(bb)                                     
        template = loader.get_template('rig/annu.html')
        return render(request, 'rig/annu.html', context)

    template = loader.get_template('rig/annuaires.html')
    return render(request, 'rig/annuaires.html', context)


    
