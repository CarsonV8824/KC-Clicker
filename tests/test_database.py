from src.database.database import Database
import pytest
def test_add_and_get_user():
    game_state = {
            "money": 0, 
            "producers": {
                "39th street owned": 0, "$PerSec": 0, "cost": 100
                }
            }
    db = Database(':memory:')  
    db.clear_data()
    db.add_data('testuser', '1234567890@example.com', game_state)
    test = db.get_data()
    db.close()
    assert test == (1, 'testuser', '1234567890@example.com', game_state)
    
def test_multiple_entries():
    
    db = Database(':memory:')  
    db.clear_data()
    game_state_1 = {
            "money": 0, 
            "producers": {
                "39th street owned": 0, "$PerSec": 0, "cost": 100
                }
            }
    
    db.add_data('testuser1', 'testuser1_1234567890@example.com', game_state_1)

    game_state_2 = {
            "money": 10, 
            "producers": {
                "39th street owned": 1, "$PerSec": 5, "cost": 150
                }
    }
    db.add_data('testuser2', 'testuser2_1234567890@example.com', game_state_2)

    test = db.get_data()
    db.close()
    assert test == (2, 'testuser2', 'testuser2_1234567890@example.com', game_state_2)
