# Generated by Django 3.0 on 2019-12-14 17:19
import json
import os

from django.db import migrations, transaction


def populate_models(apps, schema_editor):
    # Pull in the model this way to prevent using a model that could have potential
    # newer changes, which would be breaking in a larger production environment
    StateCapital = apps.get_model('state_capitals', 'StateCapital')

    # Use this files path as a relative point to grab the json data
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'data/us_state_capitals.json')
    with open(filename) as file:
        capital_data = json.load(file)

    # Bulk create instances to reduce any latency
    model_instances = []
    for abbr, data in capital_data.items():
        model_instances.append(StateCapital(**data))

    with transaction.atomic():
        StateCapital.objects.bulk_create(model_instances)


class Migration(migrations.Migration):

    dependencies = [
        ('state_capitals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_models)
    ]
