{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":1,"column":0},"end":{"row":1,"column":40},"action":"insert","lines":["from .models import Order, OrderLineItem"],"id":2}],[{"start":{"row":1,"column":40},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":0},"end":{"row":10,"column":38},"action":"insert","lines":["class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","    ","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","    ","admin.site.register(Order, OrderAdmin)"],"id":4}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":10,"column":38},"end":{"row":10,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564944385260,"hash":"b41c25037b4d40c0e47e606d335488eb4409f260"}