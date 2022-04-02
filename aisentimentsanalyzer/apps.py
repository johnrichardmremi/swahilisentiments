from django.apps import AppConfig
import os
from django.conf import settings
import pickle


class AisentimentsanalyzerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'

    name = 'aisentimentsanalyzer'
    # the name attribute is mandatory if removed there will be error
    # This attribute defines which application the configuration applies to.
    # It must be set in all AppConfig subclasses.

    path = os.path.join(settings.MODELS, 'model.p')

    # load models into separate variables
    # this will be accessible via this class
    with open(path, 'rb') as pickled:
        data = pickle.load(pickled)
    model = data['model']
    vectorize = data['vectorizer']
