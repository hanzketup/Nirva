import csv

from django.apps import apps

Offer = apps.get_model('dashBoard', 'Offer')


def gen_report(to, pk):
    writer = csv.writer(to)

    writer.writerow(
        ['ID', 'Full Name', 'Qty', 'Village', 'Region', 'Group', 'Group ID', 'Lat', 'Long'])  # Write header

    for i in Offer.objects.get(pk=pk).answers.all():
        try:
            grp = i.user.first().groups.first().name
        except:
            grp = ""

        writer.writerow([i.user.first().pk,
                         (i.user.first().first + ' ' + i.user.first().last),
                         i.value,
                         i.user.first().village,
                         i.user.first().region,
                         grp,
                         i.user.first().gps_lat,
                         i.user.first().gps_long,
                         ])

    return writer
