from .test_setup import TestSetupLoged, TestSetupAnonymous, create_game
import logging


class TestViewLogged(TestSetupLoged):
    fixtures = ["api/fixtures/dump.json"]

    def test_get_game_1(self):
        request = self.client.get(
            "/api/videogame/75",
            content_type="application/json",
            secure=True,
        )
        self.assertEqual(request.status_code, 200)


class TestViewAnonymous(TestSetupAnonymous):
    def test_get_all_videogames(self):
        request = self.client.get(
            "/api/videogames",
            content_type="application/json",
            secure=True,
        )
        self.assertEqual(request.status_code, 200)
