# Generated by Django 2.1.7 on 2019-09-05 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PID', '0002_auto_20190905_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PID.Agency'),
        ),
    ]
