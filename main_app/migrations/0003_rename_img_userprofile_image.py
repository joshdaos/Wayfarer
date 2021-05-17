from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='img',
            new_name='image',
        ),
    ]
