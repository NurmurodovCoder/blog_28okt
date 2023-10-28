from .models import Person

def person_data(request):
    person = Person.objects.first

    context = {
        'person':person
    }

    return context