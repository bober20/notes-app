from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Note
from .forms import NoteForm


def show_index_page(request):
    return redirect("notes:login")


def show_home_page(request):
    notes = Note.objects.all().filter(user=request.user)

    # print(notes[0].slug)

    data = {
        'notes': notes,
    }

    return render(request, 'notes/home.html', data)


def show_info(request, slug):
    note = get_object_or_404(Note, slug=slug)

    data = {
        "title": note.title,
        "content": note.content,
        "date": note.time_of_creation,
    }

    return render(request, "notes/note_info.html", data)


def delete_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    note.delete()

    notes = Note.objects.all()

    data = {
        "notes": notes
    }

    return render(request, 'notes/home.html', data)


def edit_note(request, slug):
    if request.method == "GET":
        note = get_object_or_404(Note, slug=slug)
        form = NoteForm(initial={
            'title': note.title,
            'content': note.content,
            'slug': note.slug,
            'time_of_creation': note.time_of_creation,
        })

        note.delete()

        data = {
            "form": form,
        }

        return render(request, 'notes/add_note.html', data)

    else:
        form = NoteForm(request.POST)

        if form.is_valid():
            note_object = form.save(commit=False)
            note_object.user = request.user
            note_object.save()
            # print(form.cleaned_data)
            return redirect("notes:home_page")

        form.add_error(None, "An error has occurred")

        data = {
            "form": form,
        }

        return render(request, 'notes/add_note.html', data)


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            try:
                note_object = form.save(commit=False)
                note_object.user = request.user
                note_object.save()

                return redirect("notes:home_page")
            except:
                form.add_error(None, "An error has occurred")

    else:
        form = NoteForm()

    data = {
        "form": form,
    }

    return render(request, 'notes/add_note.html', data)


#class AddNote(CreateView):
#     model = Note
#     fields = ['title', 'content', 'slug']
#     template_name = 'notes/add_note.html'
#     success_url = reverse_lazy('home_page')
#
#
# class UpdateNote(UpdateView):
#     model = Note
#     fields = ['title', 'content', 'slug']
#     template_name = 'notes/add_note.html'
#     success_url = reverse_lazy('notes:home_page')
