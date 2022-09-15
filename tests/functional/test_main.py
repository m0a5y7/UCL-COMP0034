from tests.functional.test_auth import login


def test_index_page_valid(test_client):
    """
    GIVEN a Flask application is running
    WHEN the '/' home page is requested (HTTP GET request)
    THEN a success response code (200) is received ()
    """
    response = test_client.get('/')
    assert response.status_code == 200


def test_blog_page_valid(test_client):
    """
    GIVEN a Flask application is running
    WHEN the '/blog' blog page is requested (HTTP GET request)
    THEN a success response code (200) is received ()
    """
    response = test_client.get('/blog')
    assert response.status_code == 200