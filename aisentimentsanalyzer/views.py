from django.shortcuts import render
from .apps import AisentimentsanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView


class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':
            # get text from request
            tweet = request.GET.get('text')

            # vectorize text
            vector = AisentimentsanalyzerConfig.vectorize.transform([tweet])

            # predict based on vector
            prediction = AisentimentsanalyzerConfig.model.predict(vector)[0]

            # build response
            response = {'tweet_sentiment': prediction}

            # return response
            return JsonResponse(response)
