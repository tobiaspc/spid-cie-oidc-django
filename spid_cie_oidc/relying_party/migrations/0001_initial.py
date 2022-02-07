# Generated by Django 4.0.2 on 2022-02-06 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OidcAuthenticationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255)),
                ('state', models.CharField(default='state-is-unique', max_length=255, unique=True)),
                ('endpoint', models.URLField(blank=True, null=True)),
                ('issuer', models.CharField(blank=True, max_length=255, null=True)),
                ('issuer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('provider_jwks', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
                ('successful', models.BooleanField(default=False)),
                ('provider_configuration', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OidcAuthenticationToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('access_token', models.TextField(blank=True, null=True)),
                ('id_token', models.TextField(blank=True, null=True)),
                ('scope', models.CharField(blank=True, max_length=255, null=True)),
                ('token_type', models.CharField(blank=True, max_length=255, null=True)),
                ('expires_in', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('logged_out', models.DateTimeField(blank=True, null=True)),
                ('authz_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spid_cie_oidc_relying_party.oidcauthenticationrequest')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
