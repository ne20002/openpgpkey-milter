import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import Milter
from Milter.test import TestBase

# create a functional empty Milter class for first tests
class EmptyMilter(Milter.Base):
    def __init__(self):
        self.fp = StringIO()
        self.fp.write(''.encode())
        self.fp.seek(0)

    def eom(self):
        print ("Test   ")
        return 'processed'

    def close(self):
        self.fp.close()

# create a test based on Milter.test.TestBase to test a Milter
class TestEmptyMilter(TestBase):
    def setUp(self):
        self.milter = EmptyMilter()
        self.milter.fp.write(''.encode())
        self.milter.fp.seek(0)

    def test_eom(self):
        self.assertEqual(self.milter.eom(), 'processed')

    def test_close(self):
        self.milter.close()
        self.assertTrue(self.milter.fp.closed)

    def test_header(self):
        self.milter.addheader('X-Test', 'test')
        self.milter.fp.seek(0)
        self.assertEqual(self.milter.fp.read(), b'X-Test: test\n')

    def test_body(self):
        self.milter.addbody('test')
        self.milter.fp.seek(0)
        self.assertEqual(self.milter.fp.read(), b'test')

    def test_eoh(self):
        self.milter.eoh()
        self.assertTrue(self.milter.headers)

    def test_envfrom(self):
        self.milter.envfrom('')

# run the test for the EmptyMilter
def test_addheader_multiple(self):
    self.milter.addheader('X-Test1', 'test1')
    self.milter.addheader('X-Test2', 'test2')
    self.milter.fp.seek(0)
    self.assertEqual(self.milter.fp.read(), b'X-Test1: test1\nX-Test2: test2\n')

def test_addheader_duplicate(self):
    self.milter.addheader('X-Test', 'test1')
    self.milter.addheader('X-Test', 'test2')
    self.milter.fp.seek(0)
    self.assertEqual(self.milter.fp.read(), b'X-Test: test1\ntest2\n')

def test_addbody_multiple(self):
    self.milter.addbody('test1')
    self.milter.addbody('test2')
    self.milter.fp.seek(0)
    self.assertEqual(self.milter.fp.read(), b'test1test2')

def test_addbody_empty(self):
    self.milter.addbody('')
    self.milter.fp.seek(0)
    self.assertEqual(self.milter.fp.read(), b'')

def test_eoh_no_headers(self):
    self.milter.eoh()
    self.assertFalse(self.milter.headers)

def test_envrcpt(self):
    self.milter.envrcpt('')
    # Add assertions for the envrcpt method if needed
