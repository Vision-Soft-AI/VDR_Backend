from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Shirt, Pant
from video_processing import process_video

def clothing_selection_view(request):
    shirts = Shirt.objects.all()
    pants = Pant.objects.all()
    
    return render(request, 'clothing_selection.html', {
        'shirts': shirts,
        'pants': pants
    })

def try_on_clothes(request):
    shirts = Shirt.objects.all()
    pants = Pant.objects.all()

    if request.method == 'POST':
        shirt_id = request.POST.get('shirt')
        pant_id = request.POST.get('pant')

        shirt = get_object_or_404(Shirt, id=shirt_id)
        pant = get_object_or_404(Pant, id=pant_id)

        # Call the video processing function
        process_video(shirt.image.path, pant.image.path)

        return render(request, 'try_on.html', {'shirts': shirts, 'pants': pants, 'selected_shirt': shirt, 'selected_pant': pant})

    return render(request, 'try_on.html', {'shirts': shirts, 'pants': pants})