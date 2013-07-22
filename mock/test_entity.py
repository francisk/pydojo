from entity import PlayerEntity
from entity import Player
from mock import MagicMock
from mock import Mock
from DBUtils.PooledDB import PooledDBError
from sqladapter import Adapter
import unittest


class Test_PlayerEntity(unittest.TestCase):
    def setUp(self):
        self.pe=PlayerEntity()
        self.do_mock=Adapter()
        self.mock_obj_all=[{"name":"Mike",
                   "passwd":"12345",
                   "last_login":"20131017"},
                   {"name":"Jack",
                    "passwd":"abcde",
                    "last_login":"20131018"}]
        self.mock_obj_one=[{"name":"Mike",
                   "passwd":"12345",
                   "last_login":"20131017"}]
        self.player_result={"name":"Mike",
                   "passwd":"12345",
                   "last_login":"20131017"}
    def tearDown(self):
        self.pe=None
        self.data_obj=None
        self.mock_obj_all=None
        self.mock_obj_one=None
        self.player_result=None

    def test_successful_find_all(self):
        #Mock the method
        self.do_mock.get_all=MagicMock(return_value=self.mock_obj_all)
        self.assertEqual(self.mock_obj_all,self.pe._find_all(self.do_mock))

    def test_failure_find_all(self):
        #Mock the method
        self.do_mock.get_all=MagicMock(return_value=False)
        self.assertEqual(None,self.pe._find_all(self.do_mock))
        
    def test_except_find_all(self):
        #Mock the method
        self.do_mock.get_all=MagicMock(side_effect=PooledDBError("Error"))
        self.assertEqual(None,self.pe._find_all(self.do_mock))
        
    def test_successful_find_by_id(self):
        self.do_mock.get_by_id=MagicMock(return_value=self.mock_obj_one)
        self.assertEqual(self.mock_obj_one,self.pe._find_by_id(1,self.do_mock))
    def test_failure_find_by_id(self):
        self.do_mock.get_by_id=MagicMock(return_value=False)
        self.assertEqual(None,self.pe._find_by_id(100,self.do_mock))
    def test_except_find_by_id(self):
        self.do_mock.get_by_id=MagicMock(side_effect=PooledDBError("Error"))
        self.assertEqual(None,self.pe._find_by_id("123",self.do_mock))
        
    def test_successful_update_by_id(self):
        self.do_mock.update_by_id=MagicMock(return_value=1)
        self.assertEqual(1,self.pe._update_by_id(None,1,self.do_mock))
    def test_successful_insert_one(self):
        self.do_mock.insert_one=MagicMock(return_value=1)
        
        self.assertEqual(1,self.pe._insert_one(None,self.do_mock))
    def test_failure_insert_one(self):
        self.do_mock.insert_one=MagicMock(side_effect=PooledDBError("Error"))
        self.assertEqual(-1,self.pe._insert_one(None,self.do_mock))
    def test_wrap_player(self):
        player=self.pe.wrap_player(self.player_result)
        self.assertEqual("Mike",player.name)
        self.assertEqual("12345",player.passwd)
        self.assertEqual("20131017",player.last_login)
    def test_wrap_result(self):
        result = self.pe.wrap_result(self.mock_obj_all)
        self.assertEqual(2, len(list(result)))
        for player in list(result):
            self.assertEqual(Player,isinstance(player))
    def test_wrap_player_with_None_result(self):
        self.assertEqual(None,self.pe.wrap_player(None))
    def test_wrap_result_with_None_result(self):
        self.assertEqual([None], list(self.pe.wrap_result(None)))
    def test_find_all_players_with_mock_data(self):
        self.do_mock.get_all=MagicMock(return_value=self.mock_obj_all)
        self.assertEqual(2, len(self.pe.find_all_players(self.do_mock)))
    def test_find_all_players_with_None(self):
        self.do_mock.get_all=MagicMock(return_value=False)
        self.assertEqual(None,self.pe.find_all_players(self.do_mock))
if __name__ == '__main__':
    unittest.main()
