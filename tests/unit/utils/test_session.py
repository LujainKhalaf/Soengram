def test_redirect_to_sign_in_page(client):
    rv = client.get("/", follow_redirects=True)
    assert b"Sign In - Soengram" in rv.data
