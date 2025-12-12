from src.database.database import Database
import pytest
def test_add_and_get_user():
    db = Database(':memory:')  
    db.add_data('testuser', '1234567890@example.com')
    test = db.get_data()
    db.close()
    assert test == [(1, 'testuser', '1234567890@example.com')]
    
    