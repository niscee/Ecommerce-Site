# Generated by Django 3.0.5 on 2020-10-07 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_shippingaddress_finaltotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order'),
        ),
    ]