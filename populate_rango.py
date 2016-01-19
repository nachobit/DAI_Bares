import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

import django
django.setup()

from rango.models import Bares, Tapas


def populate():
    bares_cat = add_bar('Casa Antonio')

    add_tapa(barname=bares_cat, name="Lomo alioli")

    add_tapa(barname=bares_cat, name="Lomo tomate")


    # Print out what we have added to the user.
    for c in Bares.objects.all():
        for p in Tapas.objects.filter(barname=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_tapa(barname, name): #tapas
    p = Tapas.objects.get_or_create(barname=barname, name=name)[0]
    return p

def add_bar(name):  #Bar
    c = Bares.objects.get_or_create(name=name, direccion=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()