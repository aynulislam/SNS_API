# Generated by Django 2.2.5 on 2019-11-10 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snaction',
            name='action_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='action_type_name', to='general.SnActionType'),
        ),
    ]
