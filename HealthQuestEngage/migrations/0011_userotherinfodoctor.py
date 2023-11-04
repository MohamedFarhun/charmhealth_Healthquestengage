# Generated by Django 4.2.2 on 2023-10-12 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HealthQuestEngage', '0010_alter_userotherinfo_middlename'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOtherInfoDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MiddleName', models.CharField(blank=True, max_length=200)),
                ('PhoneNumber', models.BigIntegerField()),
                ('DateofBirth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Pincode', models.IntegerField()),
                ('Experience', models.CharField(choices=[('Less than 1 Year', 'Less than 1 Year'), ('1-2 Years', '1-2 Years'), ('3-5 Years', '3-5 Years'), ('More than 5 Years', 'More than 5 years')], max_length=200)),
                ('Specialist', models.CharField(max_length=200)),
                ('Degrees', models.CharField(choices=[('MBBS', 'MBBS'), ('BDS', 'BDS'), ('BAMS', 'BAMS')], max_length=200)),
                ('NeetMarks', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]