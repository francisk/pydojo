from entity import PlayerEntity
from sqladapter import Adapter


def get_all_players():
    db_obj=Adapter()
    pe=PlayerEntity()
    return pe.find_all_players(db_obj)



def change_passwd(player_id,new_passwd):
    db_obj=Adapter()
    pe=PlayerEntity()
    current_player=pe._find_by_id(player_id,db_obj)
    if not update_player("passwd",new_passwd,current_player) is None:
        return pe._update_by_id(current_player,player_id,db_obj)
    else:
        raise KeyError("No such player")

def change_name(player_id,new_name):
    db_obj=Adapter()
    pe=PlayerEntity()
    current_player = pe._find_by_id(player_id,db_obj)
    if not update_player("name",new_name,current_player) is None:
        return pe._update_by_id(current_player,player_id,db_obj)
    else:
        raise KeyError("No such player")

def update_player(key,value,current_obj):
    if not current_obj is None:
        current_obj[key]=value
        return current_obj
    else:
        return None
