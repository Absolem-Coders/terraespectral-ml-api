from django.http import JsonResponse
from rest_framework.views import APIView

import random
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os

class AiListView(APIView):
    def get(self, request, *args, **kwargs):

        ore = request.GET.get('ore')
        per_page = request.GET.get('per_page')

        model_filename = f'{ore}.pickle'  # DEFINIR CAMINHO DO MODEL
        model_fpath = os.path.join(os.path.dirname(__file__), model_filename)

        n_pins = int(per_page) # DEFINIR NÚMERO DE PINS

        MIN_LATITUDE = -73
        MAX_LATITUDE = 73
        MIN_LONGITUDE = -179
        MAX_LONGITUDE = 179

        pins = []

        with open(model_fpath, 'rb') as f:
            rf = pickle.load(f)

            while len(pins) < n_pins:

                random_data = {
                    'latitude': [random.uniform(MIN_LATITUDE, MAX_LATITUDE)],
                    'longitude': [random.uniform(MIN_LONGITUDE, MAX_LONGITUDE)]
                }

                predict_X = pd.DataFrame(random_data)
                predict = rf.predict(predict_X)

                if predict[0] == 1:
                    pins.append((predict_X['latitude'][0], predict_X['longitude'][0]))

        ai_data = {
            'ore': ore,
            'perpage': per_page,
            'pins': pins
        }

        return JsonResponse(ai_data)

