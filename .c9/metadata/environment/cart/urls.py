{"filter":false,"title":"urls.py","tooltip":"/cart/urls.py","undoManager":{"mark":13,"position":13,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["from django.conf.urls import url","from .views import view_cart, add_to_cart, adjust_cart","","urlpatterns = [","    url(r'^$', view_cart, name='view_cart'),","    url(r'^add/(?P<id>\\d+)', add_to_cart, name='add_to_cart'),","    url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),","]"],"id":1}],[{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"remove","lines":["t"],"id":2},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"remove","lines":["r"]},{"start":{"row":1,"column":51},"end":{"row":1,"column":52},"action":"remove","lines":["a"]},{"start":{"row":1,"column":50},"end":{"row":1,"column":51},"action":"remove","lines":["c"]},{"start":{"row":1,"column":49},"end":{"row":1,"column":50},"action":"remove","lines":["_"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"remove","lines":["t"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"remove","lines":["s"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"remove","lines":["u"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"remove","lines":["j"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"remove","lines":["d"]},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"remove","lines":["a"]},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":[" "]}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":[","],"id":3}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":65},"action":"remove","lines":["url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),"],"id":4},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]},{"start":{"row":5,"column":62},"end":{"row":6,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["v"],"id":5},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["i"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["e"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["w"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["_"]}],[{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["c"],"id":6},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["a"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["r"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["_"],"id":7},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["t"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["o"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["_"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["c"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["a"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["t"],"id":8}],[{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"insert","lines":[","],"id":9}],[{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"insert","lines":[" "],"id":10},{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"insert","lines":["a"]},{"start":{"row":1,"column":44},"end":{"row":1,"column":45},"action":"insert","lines":["d"]},{"start":{"row":1,"column":45},"end":{"row":1,"column":46},"action":"insert","lines":["j"]},{"start":{"row":1,"column":46},"end":{"row":1,"column":47},"action":"insert","lines":["u"]},{"start":{"row":1,"column":47},"end":{"row":1,"column":48},"action":"insert","lines":["s"]},{"start":{"row":1,"column":48},"end":{"row":1,"column":49},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":49},"action":"remove","lines":["adjust"],"id":11},{"start":{"row":1,"column":43},"end":{"row":1,"column":56},"action":"insert","lines":["adjust_cart()"]}],[{"start":{"row":1,"column":54},"end":{"row":1,"column":56},"action":"remove","lines":["()"],"id":12}],[{"start":{"row":5,"column":70},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":65},"action":"insert","lines":["url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),"],"id":14}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":65},"end":{"row":6,"column":65},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564930252219,"hash":"383c0f8b9209ae5a6f0bcac1a98152d369202179"}