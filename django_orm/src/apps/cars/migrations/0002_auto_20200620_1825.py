# Generated by Django 3.0.6 on 2020-06-20 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='DealerID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealers', to='dealers.Dealer'),
        ),
        migrations.AddField(
            model_name='car',
            name='ModelId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='cars.CarModel'),
        ),
        migrations.AddIndex(
            model_name='carmodel',
            index=models.Index(fields=['name'], name='cars_carmod_name_ef19d7_idx'),
        ),
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['Status'], name='cars_car_Status_fb503c_idx'),
        ),
    ]
