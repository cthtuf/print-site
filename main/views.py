#from django.shortcuts import render
from django.http.response import HttpResponse
from weasyprint import HTML


def index(request):
    if 'site' in request.GET:
        site = request.GET['site']
        type = request.GET['type'] if 'type' in request.GET else 'pdf'
        if type.lower() == 'png':
            png = HTML(site).write_png()
            response = HttpResponse(content=png, content_type='image/png')
            response['Content-Disposition'] = 'filename=%s.png' % (
                site.split('://')[1].split('/')[0].split('?')[0]
            )

            return response
        else:
            pdf = HTML(site).write_pdf()
            response = HttpResponse(content=pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'filename=%s.pdf' % (
                site.split('://')[1].split('/')[0].split('?')[0]
            )

            return response
    else:
        return HttpResponse("Example of using: "
                                     "/?site=lalala.la&type=png or "
                                     "/?site=blablabla&type=pdf")