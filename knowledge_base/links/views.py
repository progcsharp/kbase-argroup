from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, FileResponse

from links.forms import LinkForm
from links.models import Articles, Tag


def index(request):
    data = Articles.objects.all()
    tags = Tag.objects.all()

    return render(request, "index.html", {"tags": tags, "data": data})

    # response = HttpResponse(file, content_type='text/plain')
    # response['Content-Disposition'] = 'attachment; filename=%s' % file
    # return FileResponse(
    #     file.open(),
    #     as_attachment=True,
    #     filename=file.name
    # )


def search(request):
    data = Articles.objects.all()
    if request.method == 'POST':

        name = dict(request.POST)["name"][0]
        filters = list(dict(request.POST).keys())

        data = Articles.objects.filter(
            Q(name__icontains=name) | Q(description__icontains=name) | Q(article__icontains=name))

        if filters[2:]:
            data = data.filter(Q(tags__id__in=filters[2:]))

    tags = Tag.objects.all()

    return render(request, "search.html", {"tags": tags, "data": data})


def article(request, article_id):
    article = Articles.objects.filter(id=article_id).first()
    return render(request, "article.html", {"article": article})


def download(request, article_id):
    article = Articles.objects.filter(id=article_id)
    file = article.files
    print(file, file.name)
    return FileResponse(
        file.open(),
        as_attachment=True,
        filename=file.name
    )

