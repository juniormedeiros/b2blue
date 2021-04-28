from configparser import ConfigParser
from django.shortcuts import render
from .utils import is_integer, is_number
import tmdbsimple as tmdb

config = ConfigParser()
config.read('movies/config.cfg')
tmdb.API_KEY = config['tmdb']['API_KEY']


def home(request):
    query = str(request.GET.get('query', ''))
    if query != '':
        if is_integer(query) and len(query) == 4:
            search_result = tmdb.Discover().tv(language='pt-BR', first_air_date_year=query, page=1)['results']
        elif is_number(query):
            search_result = get_discover_result()
            search_result = list(filter(lambda v: float(v['popularity']) >= float(query), search_result))
        else:
            search_result = tmdb.Search().tv(language='pt-BR', query=query)['results']
        frontend = {
            "search_result": sorted(search_result, key=lambda x: x['popularity'], reverse=True),
            "has_result": (search_result != [])
        }
    else:
        search_result = tmdb.TV().top_rated()
        frontend = {
            "search_result": search_result['results'],
            "has_result": (search_result != [])
        }
    return render(request, "movie.html", frontend)


def details(request, id=None):
    rating = str(request.GET.get('rating', ''))
    tv = tmdb.TV(id)

    success_rating = False

    if rating and id:
        guest_session_id = tmdb.account.Authentication().guest_session_new()['guest_session_id']
        success_rating = tv.rating(guest_session_id=guest_session_id, value=float(rating))['success']

    trailers = list(filter(lambda v: v['type'] == 'Trailer', tv.videos(language='pt-BR')['results']))
    teasers = list(filter(lambda v: v['type'] == 'Teaser', tv.videos(language='pt-BR')['results']))
    keywords = list(v['name'] for v in tv.keywords()['results'])

    frontend = {
        "info": tv.info(language='pt-BR'),
        "year": tv.first_air_date[0:4],
        "cast": tv.credits(language='pt-BR')['cast'][:15],
        "crew": tv.credits(language='pt-BR')['crew'][:15],
        "trailers": trailers,
        "teasers": teasers,
        "keywords": keywords,
        "reviews": tv.reviews(language='pt-BR')['results'][0:5],
        "popularity": tv.popularity,
        "success_rating": success_rating
    }
    return render(request, "details.html", frontend)


def get_discover_result():
    result = tmdb.Discover().tv(language='pt-BR', sort_by='popularity.desc', page=1)['results']
    result += tmdb.Discover().tv(language='pt-BR', sort_by='popularity.desc', page=2)['results']
    result += tmdb.Discover().tv(language='pt-BR', sort_by='popularity.desc', page=3)['results']
    result += tmdb.Discover().tv(language='pt-BR', sort_by='popularity.desc', page=4)['results']
    result += tmdb.Discover().tv(language='pt-BR', sort_by='popularity.desc', page=5)['results']
    return result
