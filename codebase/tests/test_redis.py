"""
Should run docker-compose up -d before running this test

# import pytest
# import sys

# sys.path.append(".")

# from src.module.cache.redis import RedisCache
# from src.core.config import CustomSettings


# @pytest.fixture(scope="function")
# def get_redis_cache_fixture():
#     cache = RedisCache(CustomSettings().REDIS_URL)
#     return cache


# def test_redis_add_cache(get_redis_cache_fixture):
#     get_redis_cache_fixture.clear()
#     get_redis_cache_fixture.get("key1")
#     get_redis_cache_fixture.add("value1")
#     assert get_redis_cache_fixture.get("key1") == ["value1"]


# def test_redis_add_cache2(get_redis_cache_fixture):
#     get_redis_cache_fixture.get("key1")
#     get_redis_cache_fixture.add("value2")
#     assert get_redis_cache_fixture.get("key1") == ["value1", "value2"]


# def test_redis_delete_cache(get_redis_cache_fixture):
#     get_redis_cache_fixture.delete("key1")
#     assert get_redis_cache_fixture.delete("key1") is None
"""
