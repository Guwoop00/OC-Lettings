from django.db import migrations

def copy_letting_data(apps, schema_editor):
    Letting = apps.get_model('lettings', 'Letting')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    Address = apps.get_model('lettings', 'Address')
    OldAddress = apps.get_model('oc_lettings_site', 'Address')

    for old_letting in OldLetting.objects.all():
        new_address = Address.objects.create(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city,
            state=old_letting.address.state,
            zip_code=old_letting.address.zip_code,
            country_iso_code=old_letting.address.country_iso_code
        )
        Letting.objects.create(
            title=old_letting.title,
            address=new_address
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_letting_data),
    ]