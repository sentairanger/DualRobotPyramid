import unittest

from pyramid import testing

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'', res.body)
    
    def test_forward(self):
        res = self.testapp.get('/forward', status=200)
        self.assertIn(b'', res.body)
        
    def test_backward(self):
        res = self.testapp.get('/backward', status=200)
        self.assertIn(b'', res.body)
    def test_left(self):
        res = self.testapp.get('/left', status=200)
        self.assertIn(b'', res.body)
    def test_right(self):
        res = self.testapp.get('/right', status=200)
        self.assertIn(b'', res.body)
    def test_stop(self):
        res = self.testapp.get('/stop', status=200)
        self.assertIn(b'', res.body)
    def test_north(self):
        res = self.testapp.get('/directionone', status=200)
        self.assertIn(b'', res.body)
        
    def test_south(self):
        res = self.testapp.get('/directiontwo', status=200)
        self.assertIn(b'', res.body)
    def test_west(self):
        res = self.testapp.get('/directionthree', status=200)
        self.assertIn(b'', res.body)
    def test_east(self):
        res = self.testapp.get('/directionfour', status=200)
        self.assertIn(b'', res.body)
    def test_stoptwo(self):
        res = self.testapp.get('/stoptwo', status=200)
        self.assertIn(b'', res.body)
    def test_torvaldseye(self):
        res = self.testapp.get('/torvaldson', status=200)
        self.assertIn(b'', res.body)
    def test_torvaldsoff(self):
        res = self.testapp.get('/torvaldsoff', status=200)
        self.assertIn(b'', res.body)
    def test_linuseye(self):
        res = self.testapp.get('/eyeon', status=200)
        self.assertIn(b'', res.body)
    def test_linusoff(self):
        res = self.testapp.get('/eyeoff', status=200)
        self.assertIn(b'', res.body)
    def test_min(self):
        res = self.testapp.get('/min', status=200)
        self.assertIn(b'', res.body)
        
    def test_mid(self):
        res = self.testapp.get('/mid', status=200)
        self.assertIn(b'', res.body)
    def test_max(self):
        res = self.testapp.get('/max', status=200)
        self.assertIn(b'', res.body)
    def test_min2(self):
        res = self.testapp.get('/min2', status=200)
        self.assertIn(b'', res.body)
        
    def test_mid2(self):
        res = self.testapp.get('/mid2', status=200)
        self.assertIn(b'', res.body)
    def test_max2(self):
        res = self.testapp.get('/max2', status=200)
        self.assertIn(b'', res.body)
    def test_thirty(self):
        res = self.testapp.get('/thirty', status=200)
        self.assertIn(b'', res.body)
    def test_fifty(self):
        res = self.testapp.get('/fifty', status=200)
        self.assertIn(b'', res.body)
    def test_full(self):
        res = self.testapp.get('/full', status=200)
        self.assertIn(b'', res.body)
    def test_thirty2(self):
        res = self.testapp.get('/thirty2', status=200)
        self.assertIn(b'', res.body)
    def test_fifty2(self):
        res = self.testapp.get('/fifty2', status=200)
        self.assertIn(b'', res.body)
    def test_full2(self):
        res = self.testapp.get('/full2', status=200)
        self.assertIn(b'', res.body)
    
    