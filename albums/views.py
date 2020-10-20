from django.shortcuts import render
from .models import Albums

# Create your views here.
def list_albums(request):
    albums = Albums.objects.all()
    return render(request, "Albums/list_albums.html",
                  {"albums": albums})


def add_album(request):
    if request.method == 'GET':
    else:
        form = AlbumForm(data=request.POST)
        if form.is.valid():
            form.save
            return redirect(to='list_albums')

    return render(request, "albums/add_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
        else:
            form = AlbumForm(data=request.POST, isinstance=album)
            if form.is.valid():
                form.save()
                return redirect(to='list_albums')

return render(request, "albums/edit_album.html",{
    "form": form,
    "album": album
})