from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.http import Http404
from django.utils.translation import gettext as _

from photos.models import Photo
from .services import get_photo, get_photos

import json


# Create your views here.
class FavoritesListView(ListView):
    context_object_name = 'photo_list'
    template_name = 'photos/photo_list.html'
    queryset = Photo.objects.filter(favorite=True)


class PhotoListView(ListView):
    context_object_name = 'photo_list'
    template_name = 'photos/photo_list.html'

    def get_queryset(self):
        photos = get_photos()
        photos = [{'id_unsplash': x['id'], 'preview': x['urls']['small'], 'favorite': True} if Photo.objects.filter(id_unsplash=x['id'], favorite=True).exists() else {'id_unsplash': x['id'], 'preview': x['urls']['small']} for x in photos]
        return photos


class PhotoDetailView(DetailView):
    context_object_name = 'photo'
    template_name = 'photos/photo_detail.html'

    def get_queryset(self):
        photos = [get_photo(self.kwargs['pk'])]
        return photos

    def get_object(self, queryset=None):
        if self.get_queryset()[0]:
            queryset_ = self.get_queryset()[0]
            if queryset_:
                queryset_['id_unsplash'] = self.kwargs['pk']
                queryset_['preview'] = queryset_['urls']['small']
                if Photo.objects.filter(id_unsplash=self.kwargs['pk'], favorite=True).exists():
                    queryset_['favorite'] = True  
                else: 
                    queryset_['favorite'] = False
            return queryset_
        raise Http404(_("No %(verbose_name)s found matching the query") % {'verbose_name': 'Photo'})
        


class PhotoQueryView(ListView):
    context_object_name = 'photo_list'
    template_name = 'photos/photo_list.html'

    def get_queryset(self):
        photos = get_photos(self.request.GET['search'])['results']
        photos = [{'id_unsplash': x['id'], 'preview': x['urls']['small'], 'favorite': True} if Photo.objects.filter(id_unsplash=x['id'], favorite=True).exists() else {'id_unsplash': x['id'], 'preview': x['urls']['small']} for x in photos]
        return photos


def add_favorite_photo(request, *args, **kwargs):
    data = json.loads(request.body)
    try:
        photo = Photo.objects.get(id_unsplash=data['id_unsplash'])
        photo.favorite = data['favorite']
        photo.save()
    except Photo.DoesNotExist:
        photo = Photo(**data)
        photo.save()
    except:
        return JsonResponse({'status': 404})
    return JsonResponse({'status': 200})