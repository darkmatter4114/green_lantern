from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'NewsLetter',
                'verbose_name_plural': 'NewsLetters',
                'ordering': ['email'],
            },
        ),
    ]