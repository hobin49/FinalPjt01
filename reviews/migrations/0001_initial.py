# Generated by Django 3.2.13 on 2022-11-02 15:35

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sorted', models.IntegerField(choices=[(1, '양식'), (2, '중식'), (3, '한식'), (4, '일식')], default=None)),
                ('runtime', models.CharField(max_length=100)),
                ('closing', models.CharField(max_length=100)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('hits', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('want_go', models.ManyToManyField(related_name='liked_user', to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('grade', models.IntegerField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], default=None)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
