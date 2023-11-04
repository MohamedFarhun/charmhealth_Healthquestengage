# Generated by Django 4.2.2 on 2023-11-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthQuestEngage', '0043_doctormooddiary_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Age', models.PositiveIntegerField()),
                ('Weight', models.FloatField()),
                ('Height', models.FloatField()),
                ('BloodPressure', models.PositiveIntegerField()),
                ('Cholesterol', models.PositiveIntegerField()),
                ('ExerciseHours', models.PositiveIntegerField()),
                ('Smoking', models.PositiveIntegerField(choices=[(1, 'Yes'), (0, 'No')], max_length=255)),
                ('AlcoholConsumption', models.PositiveIntegerField(choices=[(1, 'Yes'), (0, 'No')], max_length=255)),
                ('Diet', models.PositiveIntegerField(choices=[(1, 'Vegetarian'), (0, 'Non-Vegetarian')], max_length=255)),
                ('SleepHours', models.PositiveIntegerField()),
                ('StressLevel', models.PositiveIntegerField(choices=[(1, 'Medium'), (0, 'Low'), (2, 'High')], max_length=255)),
            ],
        ),
    ]