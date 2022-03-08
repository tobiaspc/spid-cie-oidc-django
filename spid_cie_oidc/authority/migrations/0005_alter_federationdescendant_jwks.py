# Generated by Django 4.0.2 on 2022-03-06 23:11

from django.db import migrations, models
import spid_cie_oidc.entity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_authority', '0004_federationdescendant_jwks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='federationdescendant',
            name='jwks',
            field=models.JSONField(default=list, help_text='a list of public keys', validators=[spid_cie_oidc.entity.validators.validate_public_jwks]),
        ),
    ]