# Generated by Django 3.0.6 on 2020-06-15 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('carId', models.AutoField(primary_key=True, serialize=False)),
                ('EngineType', models.CharField(max_length=16, null=True)),
                ('PopulationType', models.CharField(max_length=20, null=True)),
                ('Price', models.PositiveIntegerField(default=0)),
                ('FuelType', models.CharField(max_length=10, null=True)),
                ('Status', models.CharField(max_length=10, null=True)),
                ('Doors', models.PositiveIntegerField(default=2)),
                ('Capacity', models.CharField(max_length=10, null=True)),
                ('GearCase', models.CharField(max_length=10, null=True)),
                ('Number', models.CharField(max_length=16, unique=True)),
                ('Slug', models.SlugField(max_length=75)),
                ('SittingPlace', models.PositiveIntegerField(default=2)),
                ('FirstRegistrationDate', models.DateField(auto_now_add=True)),
                ('EnginePower', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('BrandId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('Logo', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Car brand',
                'verbose_name_plural': 'Car brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('ModelId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Car model',
                'verbose_name_plural': 'Car models',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('ColorId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.AddIndex(
            model_name='color',
            index=models.Index(fields=['name'], name='cars_color_name_95ff05_idx'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='BrandId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.CarBrand'),
        ),
        migrations.AddIndex(
            model_name='carbrand',
            index=models.Index(fields=['name'], name='cars_carbra_name_e5d8f6_idx'),
        ),
        migrations.AddField(
            model_name='car',
            name='ColorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Color'),
        ),
    ]
