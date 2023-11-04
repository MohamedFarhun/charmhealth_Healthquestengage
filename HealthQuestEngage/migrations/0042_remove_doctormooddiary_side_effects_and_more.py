# Generated by Django 4.2.2 on 2023-11-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthQuestEngage', '0041_doctormooddiary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctormooddiary',
            name='side_effects',
        ),
        migrations.AddField(
            model_name='doctormooddiary',
            name='patients',
            field=models.CharField(default=0),
            preserve_default=False,
        ),
    ]