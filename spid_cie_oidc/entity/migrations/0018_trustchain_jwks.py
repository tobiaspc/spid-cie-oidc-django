# Generated by Django 4.0.5 on 2022-07-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0017_remove_federationentityconfiguration_jwks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trustchain',
            name='jwks',
            field=models.JSONField(default=[], help_text='jwks of this federation entity'),
            preserve_default=False,
        ),
    ]