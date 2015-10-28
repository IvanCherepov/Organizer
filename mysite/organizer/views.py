from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LinkForm, ListForm
from .models import Link, List

def lists_all(request):
    lists = List.objects.order_by('-date_created')
    if request.GET.get('tag'):
        lists = lists.filter(tags__name=request.GET['tag'])
    context = {'lists': lists}
    return render(request, 'organizer/lists_all.html', context)

def list_details(request, list_id):
  list_a = get_object_or_404(List, pk = list_id)
  context = {'list': list_a}
  return render(request, 'organizer/list_details.html', context)

def link_details(request):
    links = Link.public.all()
    if request.GET.get('tag'):
        links = links.filter(tags__name=request.GET['tag'])
    context = {'links': links}
    return render(request, 'organizer/link_details.html', context)


def link_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        links = user.links.all()
    else:
        links = Link.public.filter(owner__username=username)
    if request.GET.get('tag'):
        links = links.filter(tags__name=request.GET['tag'])
    context = {'links': links, 'owner': user}
    return render(request, 'organizer/link_user.html', context)

def list_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        lists = user.lists.all()
    else:
        lists = Link.public.filter(owner__username=username)
    if request.GET.get('tag'):
        lists = lists.filter(tags__name=request.GET['tag'])
    context = {'lists': lists, 'owner': user}
    return render(request, 'organizer/list_user.html', context)


@login_required
def link_add(request, pk):
    list_a = get_object_or_404(List, pk = pk)

    if request.method == 'POST':
        form = LinkForm(data=request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.owner = request.user
            link.save()
            form.save_m2m()
            list_a.links.add(link)
            return redirect('organizer_list_details',
                list_id = pk)
    else:
        form = LinkForm()
    context = {'form': form, 'create': False}
    
    return render(request, 'organizer/form.html', context)

@login_required
def link_edit(request, pk_link, pk_list):
    link = get_object_or_404(Link, pk = pk_link)
    # list_a = get_object_or_404(List, pk = pk_list)
    if link.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = LinkForm(instance=link, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_list_details',
                list_id = pk_list)
    else:
        form = LinkForm(instance = link)
    context = {'form': form, 'create': False}
    return render(request, 'organizer/form.html', context)

@login_required
def link_delete(request, pk_link, pk_list):
    link = get_object_or_404(Link, pk = pk_link)
    if link.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    link.delete()
    return redirect('organizer_list_details',
                list_id = pk_list)

@login_required
def list_create(request):
    if request.method == 'POST':
        form = ListForm(data=request.POST)
        if form.is_valid():
            list_a = form.save(commit=False)
            list_a.owner = request.user
            list_a.save()
            form.save_m2m()
            return redirect('organizer_list_user',
                username=request.user.username)
    else:
        form = ListForm()
    context = {'form': form, 'create': True}
    return render(request, 'organizer/form.html', context)


@login_required
def list_edit(request, pk_list):
    list_a = get_object_or_404(List, pk = pk_list)
    if list_a.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ListForm(instance=list_a, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_list_user',
                username=request.user.username)
    else:
        form = ListForm(instance=list_a)
    context = {'form': form, 'create': False}
    return render(request, 'organizer/form.html', context)