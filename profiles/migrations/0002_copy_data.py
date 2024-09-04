from django.db import migrations

def copy_profile_data(apps, schema_editor):
    Profile = apps.get_model('profiles', 'Profile')
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')

    for old_profile in OldProfile.objects.all():
        Profile.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_profile_data),
    ]