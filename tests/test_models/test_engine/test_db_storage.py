import unittest
from models import storage
from models.state import State

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        """Set up for the tests."""
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Tear down after tests."""
        self.state.delete()

    def test_get(self):
        """Test the get method."""
        state_id = self.state.id
        self.assertEqual(storage.get(State, state_id), self.state)
        self.assertIsNone(storage.get(State, "nonexistent_id"))

    def test_count(self):
        """Test the count method."""
        initial_count = storage.count()
        initial_state_count = storage.count(State)
        state = State(name="Nevada")
        state.save()
        self.assertEqual(storage.count(), initial_count + 1)
        self.assertEqual(storage.count(State), initial_state_count + 1)

if __name__ == "__main__":
    unittest.main()

