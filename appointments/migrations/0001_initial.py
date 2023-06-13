# Generated by Django 4.2.2 on 2023-06-13 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nhs_number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('postcode', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Clinician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.department')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=9)),
                ('time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('postcode', models.CharField(max_length=8)),
                ('uuid', models.CharField(max_length=36)),
                ('clinician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.clinician')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.department')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.patient')),
            ],
        ),
    ]
