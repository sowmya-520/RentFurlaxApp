# Generated by Django 4.1.13 on 2024-02-06 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RentFurlaxApp', '0003_alter_customer_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('condition', models.CharField(max_length=255)),
                ('noofdays', models.IntegerField()),
                ('options', models.JSONField()),
                ('rentaloptions', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentFurlaxApp.category')),
            ],
        ),
    ]
