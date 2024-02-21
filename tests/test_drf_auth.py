
import pytest
from drf_auth.drf_auth import drf_auth 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = drf_auth()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = drf_auth(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

