import json

import pytest

from exam.models import Movie


# @pytest.mark.django_db
# def test_add_movie(client):
#     movies = Movie.objects.all()
#     assert len(movies) == 0
#
#     resp = client.post(
#         "/api/movies/",
#         {
#             "title": "The Big Lebowski",
#             "genre": "comedy",
#             "year": "1998",
#         },
#         content_type="application/json"
#     )
#     assert resp.status_code == 201
#     assert resp.data["title"] == "The Big Lebowski"
#     print("~"*80)
#     print(resp.data)
#
#     movies = Movie.objects.all()
#     assert len(movies) == 1

@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0