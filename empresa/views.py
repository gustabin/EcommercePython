from django.shortcuts import render, redirect
from .models import Empresa
# from datetime import datetime
from django.contrib import messages

def home(request):
    empresaListado = Empresa.objects.all()
    messages.success(request, 'Empresas listadas!')
    return render(request, "gestionEmpresa.html", {"empresas": empresaListado})

def registrarEmpresa(request):
    nombre= request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    ciudad = request.POST['txtCiudad']
    estado = request.POST['txtEstado']
    pais = request.POST['txtPais']
    tituloPagina = request.POST['txtTituloPagina']
    ruta = request.POST['txtRuta']
    subdominio = request.POST['txtSubdominio']
    apodo = request.POST['txtApodo']
    email = request.POST['txtEmail']
    facebook = request.POST['txtFacebook']
    twitter = request.POST['txtTwitter']
    instagram = request.POST['txtInstagram']
    youtube = request.POST['txtYoutube']
    linkedin = request.POST['txtLinkedin']
    titulo1 = request.POST['txtTitulo1']
    titulo2 = request.POST['txtTitulo2']
    titulo3 = request.POST['txtTitulo3']
    subtitulo1 = request.POST['txtSubTitulo1']
    subtitulo2 = request.POST['txtSubTitulo2']
    subtitulo3 = request.POST['txtSubTitulo3']
    descripcion1 = request.POST['txtDescripcion1']
    descripcion2 = request.POST['txtDescripcion2']
    descripcion3 = request.POST['txtDescripcion3']
    imagen1 = request.FILES.get('txtImagen1', 'empresa/sinimagen.png')   
    imagen2 = request.FILES.get('txtImagen2', 'empresa/sinimagen.png')   
    imagen3 = request.FILES.get('txtImagen3', 'empresa/sinimagen.png')   
    direccion = request.POST['txtDireccion']
    gateway = request.POST['txtGateway']
    environment = request.POST['txtEnvironment']
    sandbox = request.POST['txtSandbox']
    produccion = request.POST['txtProduccion']
    secret = request.POST['txtSecret']
    accessToken = request.POST['txtAccessToken']
    publicaStripe = request.POST['txtPublicaStripe']
    secretaStripe = request.POST['txtSecretaStripe']
    status = request.POST['txtStatus']
    # fecha = datetime.now()

    logo    = request.FILES.get('txtLogo',    'empresa/sinImagen.png')  
    favicon = request.FILES.get('txtFavicon', 'empresa/sinImagen.png')

    empresa = Empresa.objects.create(nombre=nombre, telefono=telefono, ciudad=ciudad,
    estado=estado, pais=pais, logo=logo, favicon=favicon, tituloPagina=tituloPagina,
    ruta=ruta, subdominio=subdominio, apodo=apodo, email=email, facebook=facebook,
    twitter=twitter, instagram=instagram, youtube=youtube, linkedin=linkedin,
    titulo1=titulo1, titulo2=titulo2, titulo3=titulo3, subtitulo1=subtitulo1,
    subtitulo2=subtitulo2, subtitulo3=subtitulo3, descripcion1=descripcion1,
    descripcion2=descripcion2, descripcion3=descripcion3, imagen1=imagen1,
    imagen2=imagen2, imagen3=imagen3, direccion=direccion, gateway=gateway,
    environment=environment, sandbox=sandbox, produccion=produccion, secret=secret,
    accessToken=accessToken, publicaStripe=publicaStripe, secretaStripe=secretaStripe,
    status=status)
    messages.success(request, '¡Empresa guardada!')
    return redirect('/empresa/')

def edicionEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    return render(request, "edicionEmpresa.html", {"empresa": empresa})

def editarEmpresa(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    ciudad = request.POST['txtCiudad']

    estado = request.POST['txtEstado']
    pais = request.POST['txtPais']
    tituloPagina = request.POST['txtTituloPagina']
    ruta = request.POST['txtRuta']
    subdominio = request.POST['txtSubdominio']
    apodo = request.POST['txtApodo']
    email = request.POST['txtEmail']
    facebook = request.POST['txtFacebook']
    twitter = request.POST['txtTwitter']
    instagram = request.POST['txtInstagram']
    youtube = request.POST['txtYoutube']
    linkedin = request.POST['txtLinkedin']
    titulo1 = request.POST['txtTitulo1']
    titulo2 = request.POST['txtTitulo2']
    titulo3 = request.POST['txtTitulo3']
    subtitulo1 = request.POST['txtSubTitulo1']
    subtitulo2 = request.POST['txtSubTitulo2']
    subtitulo3 = request.POST['txtSubTitulo3']
    descripcion1 = request.POST['txtDescripcion1']
    descripcion2 = request.POST['txtDescripcion2']
    descripcion3 = request.POST['txtDescripcion3']
    
    direccion = request.POST['txtDireccion']
    gateway = request.POST['txtGateway']
    environment = request.POST['txtEnvironment']
    sandbox = request.POST['txtSandbox']
    produccion = request.POST['txtProduccion']
    secret = request.POST['txtSecret']
    accessToken = request.POST['txtAccessToken']
    publicaStripe = request.POST['txtPublicaStripe']
    secretaStripe = request.POST['txtSecretaStripe']
    status = request.POST['txtStatus']  

    empresa = Empresa.objects.get(id=id)
    empresa.nombre = nombre
    empresa.telefono = telefono
    empresa.ciudad = ciudad
    empresa.estado = estado
    empresa.pais = pais
    empresa.tituloPagina = tituloPagina
    empresa.ruta = ruta
    empresa.subdominio = subdominio
    empresa.apodo = apodo
    empresa.email = email
    empresa.facebook = facebook
    empresa.twitter = twitter
    empresa.instagram = instagram
    empresa.youtube = youtube
    empresa.linkedin = linkedin
    empresa.titulo1 = titulo1
    empresa.titulo2 = titulo2
    empresa.titulo3 = titulo3
    empresa.subtitulo1 = subtitulo1
    empresa.subtitulo2 = subtitulo2
    empresa.subtitulo3 = subtitulo3
    empresa.descripcion1 = descripcion1
    empresa.descripcion2 = descripcion2
    empresa.descripcion3 = descripcion3
   
    empresa.direccion = direccion
    empresa.gateway = gateway
    empresa.environment = environment
    empresa.sandbox = sandbox
    empresa.produccion = produccion
    empresa.secret = secret
    empresa.accessToken = accessToken
    empresa.publicaStripe = publicaStripe
    empresa.secretaStripe = secretaStripe
    empresa.status = status

    # favicon = request.FILES.get('txtFavicon', 'empresa/sinImagen.png')
    if 'txtLogo' in request.FILES:
        logo = request.FILES['txtLogo']
        empresa.logo = logo
    
    if 'txtFavicon' in request.FILES:
        favicon = request.FILES['txtFavicon']
        empresa.favicon = favicon

    if 'txtImagen1' in request.FILES:
        imagen1 = request.FILES['txtImagen1']
        empresa.imagen1 = imagen1

    if 'txtImagen2' in request.FILES:
        imagen2 = request.FILES['txtImagen2']
        empresa.imagen2 = imagen2
    
    if 'txtImagen3' in request.FILES:
        imagen3 = request.FILES['txtImagen3']
        empresa.imagen3 = imagen3

    empresa.save()
    messages.success(request, '¡Empresa actualizada!')
    return redirect('/empresa/')

def eliminacionEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.success(request, 'Empresa eliminada!')
    return redirect('/empresa/')