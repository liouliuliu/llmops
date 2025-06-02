import pytest

from pkg.http_code import HttpCode


class TestAppHandler:
    """app控制器的测试类"""
    @pytest.mark.parametrize("query", [None,"你好，你是谁？"])
    def test_completion(self,query, client):
        resp = client.post("/app/completion",json={"query":query})
        assert resp.status_code == 200
        if query is not None:
            assert resp.json.get("code") == HttpCode.SUCCESS
        else:
             assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        print("响应内容：",resp.json)