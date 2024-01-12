import pytest
import sys

sys.path.append(".")

from src.module.cache.memory import MemoryCache


@pytest.fixture(scope="function")
def get_memory_cache_fixture():
    cache = MemoryCache()
    return cache


def test_memory_cache(get_memory_cache_fixture):
    cache = get_memory_cache_fixture

    # Test set and get
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"

    # Test overwrite
    cache.set("key1", "value2")
    assert cache.get("key1") == "value2"

    # Test delete
    cache.delete("key1")
    assert cache.get("key1") is None

    # Test clear
    cache.set("key2", "value2")
    cache.clear()
    assert cache.get("key2") is None
