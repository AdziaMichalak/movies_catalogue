from unittest.mock import Mock

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking():
   result = some_function_to_mock()

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2
   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2