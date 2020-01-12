# Generated by Django 3.0.1 on 2019-12-28 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fotos',
            new_name='Foto',
        ),
        migrations.AddField(
            model_name='comentario',
            name='foto',
            field=models.ManyToManyField(help_text='Seleccione una regla para este Lugar', to='basedatos.Foto'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='foto',
            field=models.ManyToManyField(help_text='Seleccione una regla para este Lugar', to='basedatos.Foto'),
        ),
        migrations.AddField(
            model_name='noticias',
            name='foto',
            field=models.ManyToManyField(help_text='Seleccione una regla para este Lugar', to='basedatos.Foto'),
        ),
    ]
