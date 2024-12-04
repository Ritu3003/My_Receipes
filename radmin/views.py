from django.shortcuts import render, redirect
from radmin.models import Radmin

# Create your views here.
def radmin(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sdescription = request.POST.get('description')
        simage = request.FILES.get('image')  # Handle file uploads using request.FILES

        if sname and simage and sdescription:
            # Save the data to the database
            item = Radmin.objects.create(name=sname, image=simage, description=sdescription)

            # Redirect to the same page after saving to prevent form resubmission on refresh
            return redirect('radmin')  # Use the URL name of this view (defined in urls.py)

    # If request is not POST, or after redirect, display all items
    show = Radmin.objects.all()
    return render(request, 'radmin.html', {'show': show})




def rdelete(request, id):
    d = Radmin.objects.filter(id = id)
    d.delete()
    return redirect('radmin')


def redit(request, id):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sdescription = request.POST.get('description')
        simage = request.FILES.get('image')  # Handle file uploads using request.FILES
        sid = request.POST.get('id')
        if sid:
            item = Radmin.objects.get(id=sid)
            item.name = sname
            item.description = sdescription
            item.image = simage
            item.save()
            return redirect('radmin')
        else:
            pass

    e = Radmin.objects.get(id = id)
    return render(request, 'edit_recipe.html', {'e': e})
        

    


