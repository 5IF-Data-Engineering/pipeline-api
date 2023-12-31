from django.http import HttpResponse, JsonResponse, FileResponse
from rest_framework.decorators import api_view
from ingestion_weather.pipeline.extract import extract_data
from ingestion_weather.pipeline.transform import transform_data
from ingestion_weather.pipeline.load import load_data
import time
from django.core.cache import cache
from pipeline_api.settings import CACHE_TTL
import json


@api_view(['GET'])
def ingestionWeatherDataPipeline(request):
    lat = request.query_params.get('lat', None)
    lon = request.query_params.get('lon', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    daily = request.query_params.get('daily', None)
    city = request.query_params.get('city', None)

    # Check if data is already cached
    cached_key = f"ingestion_weather_data_{start_date}_{end_date}"
    cached_data = cache.get(cached_key)
    if cached_data is not None:
        returned_data = json.loads(cached_data)
        return JsonResponse(returned_data)

    # If not cached, start pipeline
    # Start pipeline
    start_time = time.time()
    # Extraction
    data = extract_data(lat, lon, start_date, end_date, daily)
    # Transformation
    transformed_data = transform_data(data, city, daily)
    # Load
    load_data(transformed_data, daily)
    processing_time = time.time() - start_time
    # Cache data
    data_to_cache = json.dumps({"processing_time": processing_time, "message": "Weather data successfully ingested"})
    cache.set(cached_key, data_to_cache, timeout=CACHE_TTL)
    return JsonResponse({"processing_time": processing_time, "message": "Weather data successfully ingested"})
