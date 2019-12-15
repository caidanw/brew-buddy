import openbrewerydb
from django.apps import apps
from rest_framework import viewsets, permissions, generics

from .models import Brewery
from .serializers import BrewerySerializer

StateCapital = apps.get_model('state_capitals', 'StateCapital')


class BreweryViewset(viewsets.ModelViewSet):
    queryset = Brewery.objects.all().order_by('id')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BrewerySerializer

    def get_queryset(self):
        queryset = Brewery.objects.all()
        capital_id = self.request.query_params.get('near_capital')

        if capital_id is not None:
            capital = StateCapital.objects.all().filter(id=capital_id)[:1].get()
            data = openbrewerydb.load(state=capital.name)
            closest_breweries = calculate_closest(data, capital)
            return closest_breweries
        else:
            return queryset.order_by('updated_at')[:10]


def calculate_closest(dataframe, capital: StateCapital):
    # First clean the data of any NaN longitudes and latitudes
    dataframe = dataframe.dropna()

    # Sort by closest longitude then latitude
    df_long = dataframe.iloc[(dataframe['longitude'] - capital.long).abs().argsort()]
    df_lat = df_long.iloc[(df_long['latitude'] - capital.lat).abs().argsort()][:5]
    return df_lat.to_dict('records')
