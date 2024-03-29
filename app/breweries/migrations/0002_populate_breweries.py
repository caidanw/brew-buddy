# Generated by Django 3.0 on 2019-12-15 01:11
import openbrewerydb
from django.db import migrations, transaction


def populate_models(apps, schema_editor):
    # Pull in the model this way to prevent using a model that could have potential
    # newer changes, which would be breaking in a larger production environment
    Brewery = apps.get_model('breweries', 'Brewery')

    # Here to give a cleaner separation of output during migrations
    print()

    # Only getting breweries in Colorado so we don't wait super long during migrations
    data = openbrewerydb.load(state='Colorado', verbose=True)
    data = data.dropna()
    data_records = data.to_dict('records')

    # Bulk create instances to reduce any latency
    model_instances = []
    for record in data_records:
        del record['id']
        del record['tag_list']
        model_instances.append(Brewery(**record))

    with transaction.atomic():
        Brewery.objects.bulk_create(model_instances)


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_models)
    ]
