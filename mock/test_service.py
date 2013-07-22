import unittest
import playerservice


class Test_playerservice(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_all_players(self):
        self.assertEqual(2, len(playerservice.get_all_players()))
    def test_changepasswd(self):
        pass
if __name__ == '__main__':
    unittest.main()
