from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rango.models import Bares, Tapas
from rango.forms import LoginForm, RegisterForm, CategoryForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def index(request):
    #return HttpResponse("Rango says hey there world!")
    context_dict = {'boldmessage': "I am bold font from the context"}

    bares_list = Bares.objects.order_by('-name')[:5]	#category_list  Bares=Category
    context_dict = {'bares': bares_list}	#bares=categories

    return render(request, 'base.html', context_dict)


def category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/category.html', {'form': form})

def bares(request):
    context_dict={}
    try:
        bar = Bares.objects.get()
        context_dict['nombre_bar']=bar.name
        context_dict['dire_bar']=bar.direccion
        tapas=Tapa.objects.filter(bar=bar)
        context_dict['tapas']=tapas
        context_dict['bar']=bar
        bar.votar()
        bar.save()
    except Bar.DoesNotExist:
        pass
    return render(request, 'rango/base.html', context_dict)

#LOGIN
def userlogin(request):
	form = LoginForm()
	context = { 'form': form, 'mensaje':'Logeandose'}

	if request.method == 'POST':		
		form = LoginForm(request.POST)		
		usuario = request.POST.get('username')
		passwd = request.POST.get('password')
		# Hacer el login
		user = authenticate(username=usuario, password=passwd)
		
		if user is not None and user.is_active:
			login(request, user)
			context['mensaje'] =  u'Logeado como  %s, password %s' % (usuario, passwd)
		else:
			context['mensaje'] =  u'No usuario  o password incorrecta'

	return render (request, 'rango/login.html', context)


def reclama_datos (request):

    bares = Bares.objects.order_by('-numero_visita')[:3]

    datos={'bares':[bares[0].nombre,bares[1].nombre,bares[2].nombre], 'visitas':[bares[0].numero_visita,bares[1].numero_visita,bares[2].numero_visita]}
     
    return JsonResponse(datos, safe=False)

def me_gusta(request,url):

    print("AQUI")

    return JsonResponse(datos, safe=False)

#REGISTRO
def registro(request):	
	form = RegisterForm()
	context = { 'mensaje': 'Estamos en  Registro', 'form': form,}

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():		
			# Save the user's form data to the database.
			user = form.save()
                       # Now we hash the password with the set_password method.
                       # Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()						
			context['mensaje'] =  u'Registrado como  %s' % (user.username)		
		else:
			context['form'] = form
	   	
	return render (request, 'rango/registro.html', context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/rango/')

##Decorador para acceso a zona restringida:
@login_required
def restricted(request):
    return HttpResponseRedirect('/rango/category/')


