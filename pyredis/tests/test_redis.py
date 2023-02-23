import pytest
import asyncio
from main import TestClass


# invalid because call from parametrize has no evenloop at all.
# @pytest.mark.parametrize('q,w', [(TestClass(), TestClass()), (TestClass(), TestClass())])
# @pytest.mark.asyncio
# async def test_event_loop(q: TestClass,w: TestClass):
#     print(q.keys())
#     assert True is True

@pytest.mark.asyncio
async def test_event_loop():
    q = TestClass()
    w = TestClass()
    print(q.keys())
    print(w.keys())
    assert True is True
