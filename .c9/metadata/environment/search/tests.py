{"filter":false,"title":"tests.py","tooltip":"/search/tests.py","undoManager":{"mark":19,"position":19,"stack":[[{"start":{"row":3,"column":0},"end":{"row":8,"column":58},"action":"insert","lines":["class TestViews(LoggedInTestCase):","","    def test_get_landing_page_view(self):","        page = self.client.get(\"/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"landing_page.html\")"],"id":2}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["s"],"id":3},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["w"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":["i"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["V"]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["S"],"id":4},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["e"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["a"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["r"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["c"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["h"]}],[{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["n"],"id":5},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["I"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["d"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["e"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":["g"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["g"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["o"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["L"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":43},"action":"insert","lines":["from django.contrib.auth.models import User"],"id":6}],[{"start":{"row":1,"column":43},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"remove","lines":["w"],"id":8},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"remove","lines":["e"]},{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"remove","lines":["i"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"remove","lines":["v"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"remove","lines":["_"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"remove","lines":["g"],"id":9},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["n"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["i"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["d"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["n"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"remove","lines":["a"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"remove","lines":["l"]}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["s"],"id":10},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["e"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["a"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["r"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["x"]}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"remove","lines":["x"],"id":11}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["c"],"id":12},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["h"]}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["s"],"id":13},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["e"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["a"]},{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["r"]},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["c"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["h"]}],[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["/"],"id":14}],[{"start":{"row":9,"column":50},"end":{"row":9,"column":51},"action":"remove","lines":["e"],"id":15},{"start":{"row":9,"column":49},"end":{"row":9,"column":50},"action":"remove","lines":["g"]},{"start":{"row":9,"column":48},"end":{"row":9,"column":49},"action":"remove","lines":["a"]},{"start":{"row":9,"column":47},"end":{"row":9,"column":48},"action":"remove","lines":["p"]},{"start":{"row":9,"column":46},"end":{"row":9,"column":47},"action":"remove","lines":["_"]},{"start":{"row":9,"column":45},"end":{"row":9,"column":46},"action":"remove","lines":["g"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"remove","lines":["n"]},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"remove","lines":["i"]},{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"remove","lines":["d"]},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"remove","lines":["n"]},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"remove","lines":["a"]},{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"remove","lines":["l"]}],[{"start":{"row":9,"column":39},"end":{"row":9,"column":40},"action":"insert","lines":["s"],"id":16},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["a"]},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"remove","lines":["r"],"id":17},{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"remove","lines":["a"]}],[{"start":{"row":9,"column":40},"end":{"row":9,"column":41},"action":"insert","lines":["e"],"id":18},{"start":{"row":9,"column":41},"end":{"row":9,"column":42},"action":"insert","lines":["a"]},{"start":{"row":9,"column":42},"end":{"row":9,"column":43},"action":"insert","lines":["r"]},{"start":{"row":9,"column":43},"end":{"row":9,"column":44},"action":"insert","lines":["c"]},{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["g"]}],[{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"remove","lines":["g"],"id":19}],[{"start":{"row":9,"column":44},"end":{"row":9,"column":45},"action":"insert","lines":["h"],"id":20}],[{"start":{"row":1,"column":0},"end":{"row":9,"column":52},"action":"remove","lines":["from django.contrib.auth.models import User","","# Create your tests here.","class TestSearch(TestCase):","","    def test_get_search_page(self):","        page = self.client.get(\"/search/\")","        self.assertEqual(page.status_code, 200)","        self.assertTemplateUsed(page, \"search.html\")"],"id":21}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":0},"end":{"row":1,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565721171506,"hash":"d127e2e002d5280a2b2bf02b95f1e230a07e0ab1"}