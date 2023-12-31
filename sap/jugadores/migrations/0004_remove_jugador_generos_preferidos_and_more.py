# Generated by Django 4.2.7 on 2023-11-26 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0003_jugador_generos_preferidos_jugador_modos_preferidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='generos_preferidos',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='modos_preferidos',
        ),
        migrations.AddField(
            model_name='jugador',
            name='generos_preferidos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jugadores.generojuego'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='modos_preferidos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jugadores.modo'),
        ),
    ]
