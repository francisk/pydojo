from DBUtils.PooledDB import PooledDBError
from sqladapter import Adapter


class PlayerEntity(object):
    
    def __init__(self):
        self._table_name="player"

    def find_all_players(self,data_obj):
        result = self._find_all(data_obj)
        player_list= filter(lambda x:not x is None,
                            list(self.wrap_result(result)))
        if len(player_list)>0:
            return player_list
        else:
            return None

    def find_player_by_id(self,id_num,data_obj):
        result = self._find_by_id(1,data_obj)
        return self.wrap_result(result)[0]
    
    def wrap_result(self,data_set):
        if not data_set is None:
            for record in data_set:
                yield self.wrap_player(record)
        else:
            yield None
            
    def wrap_player(self,record):
        if not record is None:
            player=Player()
            for key in record:
                setattr(player,key,record[key])
            return player
        else:
            return None
    
    def _find_all(self,data_obj):
        result=None
        try:
            result=data_obj.get_all(self._table_name)
        except PooledDBError: 
            pass
        if not result:
            return None
        else:
            return result
    
    def _find_by_id(self,id_num,data_obj):
        result=None
        try:
            result=data_obj.get_by_id(self._table_name,id_num)
        except PooledDBError as e:
            pass
        if not result:
            return None
        else:
            return result
    
    def _update_by_id(self,obj,id_num,data_obj):
        involved_count=0
        try:
            involved_count=data_obj.update_by_id(self._table_name,
                                                 obj,
                                                 id_num)
        except PooledDBError as e:
            involved_count=-1

        return involved_count

    def _insert_one(self,obj,data_obj):
        insert_id=0
        try:
            insert_id=data_obj.insert_one(self._table_name,
                                               obj,
                                               data_obj)
        except PooledDBError as e:
            insert_id = -1

        return insert_id

    def _delete_by_id(self,obj,id_num,data_obj):
        involved_count=0
        try:
            involved_count=data_obj.delete_by_id(self._table_name,
                                                 id_num)
        except PooledDBError as e:
            involved_count=-1
        return involved_count

class Player(object):
    def __init__(self):
        pass
