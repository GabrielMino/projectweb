from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def contact(request):    
    if request.method == 'POST':         #en este caso procesaremos el formulario
        form = ContactForm(request.POST)#aquí almacenamos los datos del formulario
        if form.is_valid():#comprobamos que los datos del formulario son válidos
            cd = form.cleaned_data
            #enviaremos el email y redireccionamos
            # Envio del mai
            email = EmailMessage (
                'Nuevo mensaje de MISITIOWEB', # Asunto
                'De {} <{}>\n\nMensaje:\n\n{}'.format(cd['name'], cd['email'], cd['message']), #Cuerpo
                EMAIL_HOST_USER,# Origen
                ['gabrielminod@gmail.com'],#Destino
                reply_to=[cd['email']],#email de respuesta
            )

            try:
                email.send()
                #si todo va ok, redireccionamos a ?ok
                return redirect(reverse('contact')+'?ok')
            except Exception as e:
                logger.error('Error enviando email: %s', e)
                
                #si algo falla, redireccionamos a ?fail
                return redirect(reverse('contact')+'?fail')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
