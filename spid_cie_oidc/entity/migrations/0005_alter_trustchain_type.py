# Generated by Django 4.0.2 on 2022-02-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_entity', '0004_alter_trustchain_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trustchain',
            name='type',
            field=models.CharField(blank=True, choices=[('openid_relying_party', 'openid_relying_party'), ('openid_provider', 'openid_provider'), ('federation_entity', 'federation_entity'), ('oauth_resource', 'oauth_resource')], default='openid_provider', help_text='OpenID Connect Federation entity type', max_length=33),
        ),
    ]
