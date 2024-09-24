from django.shortcuts import render, redirect
from .forms import AreaForm
from .models import Area  # Import the Location model

def create_location(request):
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            Area = form.save()  # Save the location with the uploaded image
            return redirect('location_view', pk=Area.pk)  # Redirect to the location detail view
            
    else:
        form = AreaForm()
        img = Area.objects.all()
    return render(request, 'location.html', {"img": img, "form": form})
