from django.shortcuts import render


def index(request):

    articles = [
        {
            'id': '1',
            'title': 'Fler vårdas på iva nu än under pandemins andra våg',
            'url': 'https://omni.se/',
            'text': 'Antalet patienter som vårdas på intensivvårdsavdelning på grund av covid-19 ökar ytterligare och är nu fler än under den så kallade andra vågen i januari, skriver TT. För närvarande får 392 patienter vård på iva på grund av covid-19, enligt intensivvårdsregistret. Den högsta noteringen under den andra vågen var 389 patienter. Siffran är dock lägre än noteringen under april 2020 då 558 patienter fick intensivvård samtidigt.',
            'score': 0
        },
        {
            'id': '2',
            'title': 'Studenter planerar för firande på båt: ”Olämpligt”',
            'url': 'https://omni.se/',
            'text': 'Studenter i Karlskrona planerar att fira studenten på skärgårdsbåtar eftersom det är förbjudet med studentflak, rapporterar P4 Blekinge. – Det är väl ungefär som att åka flak tänker vi, att vi hyr högtalare, åker runt och dansar lite, säger studenten Lowa Aronsson till P4 Blekinge. Men smittskyddsläkaren Bengt Wittesjö är kritisk och menar att båtturerna är ett ”väldigt olämpligt sätt” att fira sin student på. – Blir det ett alltför livligt firande så kommer vi att få lida för det under juni och juli, säger han.',
            'score': 0
        },
        {
            'id': '3',
            'title': 'Smittspridningen ökar på flera håll i landet efter påsk',
            'url': 'https://omni.se/',
            'text': 'Coronasmittan ökar igen i Västerbotten efter påsken – den senaste veckan har 646 positiva fall konstaterats, vilket är en ökning med 179 fall jämfört med veckan innan. Det meddelar region Västerbotten i ett pressmeddelande. ”Mycket tyder på att påskhelgen och påskledigheten har bidragit till den. Det är nu mycket viktigt att bromsa smittspridningen”, säger Stephan Stenmark, smittskyddsläkare i Region Västerbotten. Även inom region Jämtland Härjedalen syns en kraftig ökning av smittan. Under förra veckan konstaterades 607 fall av covid-19, vilket är en ökning med 52 procent jämfört med veckan innan. Av de nya kända fallen bor 79 utanför länet, skriver SVT Jämtland.',
            'score': 0
        },
        {
            'id': '4',
            'title': 'Källor: Två skjutna nära sjukhus i Paris – en död',
            'url': 'https://omni.se/',
            'text': 'En person har dött och en skadats i samband med en skottlossning utanför sjukhuset Henry Dunant i sydvästra Paris, uppger källor för flera medier. Den misstänkte skytten flydde på en moped eller motorcykel enligt Le Parisiens källor. Den andra personen uppges få vård på intensivvårdsavdelning.',
            'score': 0
        },
        {
            'id': '5',
            'title': 'Läkarfacket backar KD-förslag: Öka statens ansvar',
            'url': 'https://omni.se/',
            'text': 'Läkarförbundet välkomnar KD:s förslag att ansvaret för sjukvården ska skiftas från regionerna till staten. Det framgår av ett pressmeddelande. – Ska vi uppnå en likvärdig vård måste regionernas inflytande över vården minska (...). Pandemin har tydliggjort att statens ansvar för vården måste öka, säger Sofia Rydgren Stale ordförande Sveriges Läkarförbund. I nuläget är vården olika bra beroende på var i landet man bor, enligt organisationen.',
            'score': 0
        }
    ]

    if (request.method == "POST"):
        print(request.POST)
        if request.POST.get('like') != None:
            print(request.POST.get('like'))
            #next((item for item in articles if item['id'] == request.POST.get('like')), None)['like'] = '1'

    if (request.method == "POST"):
        if request.POST.get('dislike') != None:
            print(request.POST.get('dislike'))

    if request.GET.get('searchquery') != None:
        relevantArticles = []
        for article in articles:
            if request.GET.get('searchquery').lower() in article.get('title').lower():
                relevantArticles.append(article)
        context = {'articles': relevantArticles}
    else:
        context = {'articles': articles}

    return render(request, 'index.html', context)
