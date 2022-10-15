import pytest

from exam.models import Movie
from tests.exam.conftest import add_movie


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie =add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    resp = client.get(f"/api/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f"/api/movies/foo/")
    assert resp.status_code == 404

@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    movie_two = add_movie("No Country for Old Men", "thriller", "2007")
    resp = client.get(f"/api/movies/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == movie_one.title
    assert resp.data[1]["title"] == movie_two.title
# @pytest.mark.django_db
# def test_movie_model():
#     movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
#     movie.save()
#     assert movie.title == "Raising Arizona"
#     assert movie.genre == "comedy"
#     assert movie.year == "1987"
#     assert movie.created_date
#     assert movie.updated_date
#     assert str(movie) == movie.title
