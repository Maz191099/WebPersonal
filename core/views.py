from django.shortcuts import render, HttpResponse
html_base = """
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about-me/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
    </ul>
"""
# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <p>Portada</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Hola yo soy Miguel</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
    <h2>Contacto</h2>
    <p>Ponte en contacto conmigo a través de correo electrónico y Facebook.</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """<h2>Portafolio</h2>
    <p>Mis Trabajos</p>
    """)