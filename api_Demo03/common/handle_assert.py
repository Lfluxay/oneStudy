
class Assert:
    def assertDictIn(self, expected, res):
        for k, v in expected.items():
            if res.get(k) == v:
                pass
            else:
                raise AssertionError("{} not in {}".format(expected, res))