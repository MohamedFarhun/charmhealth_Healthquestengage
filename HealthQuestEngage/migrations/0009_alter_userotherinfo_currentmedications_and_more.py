# Generated by Django 4.2.2 on 2023-10-11 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthQuestEngage', '0008_userotherinfo_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotherinfo',
            name='CurrentMedications',
            field=models.CharField(choices=[('Tablets', 'Tablets'), ('Inhalers', 'Inhalers'), ('Injections', 'Injections')], max_length=200),
        ),
        migrations.AlterField(
            model_name='userotherinfo',
            name='MedicalConditions',
            field=models.CharField(choices=[('COVID-19', 'COVID-19'), ('Common Cold', 'Common Cold'), ('Asthma Attack', 'Asthma Attack')], max_length=200),
        ),
    ]
