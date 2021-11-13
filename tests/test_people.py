# import People Class
from people.People import People

# To test people Class, we start the test case class with Test
class TestPeople:

    def test_weight(self):
        p1 = People('Mark', 22, 130, 'CityU')
        assert p1.get_weight() == 130

        p1.lose_weight(5)
        assert p1.get_weight() == 125