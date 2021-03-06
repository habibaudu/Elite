# Generated by Django 3.0.6 on 2020-06-06 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.enumerators
import utils.id_genrator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.CharField(default=utils.id_genrator.generate_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('active', 'active'), ('deleted', 'deleted')], default='active', max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('profile_image', models.URLField(default='https://res.cloudinary.com/some_profile_image.png')),
                ('gender', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.CharField(default=utils.id_genrator.generate_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invent',
            fields=[
                ('id', models.CharField(default=utils.id_genrator.generate_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('about_invention', models.TextField(default='About your invention and possibly links to it', null=True)),
                ('invent_media', models.URLField()),
                ('state', models.CharField(choices=[(utils.enumerators.StateType['active'], 'active'), (utils.enumerators.StateType['deleted'], 'deleted')], default=utils.enumerators.StateType['active'], max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.State')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
