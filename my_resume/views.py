from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Message
from .forms import MessageForm
# Create your views here.
def home(request):
    """
    Alternative Solution 

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        new_message = Message()
        new_message.name = name
        new_message.email = email
        new_message.message = message
        new_message.save()
    """

    form = MessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, "Your message has been sent successfully.")
            return redirect("/")

    return render(request, 'index.html', {'form': form,})