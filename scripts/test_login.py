import pytest
class Testlogin():

    def test_login_001(self):
        print('test002')
        assert 1

    def test_login_002(self):
        print('test001')
        assert 1


    def test_login_003(self):
        print('test001')
        assert 0
        

    def test_login_004(self):
        print('test001')
        assert 1

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])