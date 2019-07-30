{"filter":false,"title":"forms.py","tooltip":"/issues/forms.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":13,"column":29},"action":"insert","lines":["from django import forms","from .models import Issue, Comment, Reply","","","class IssueForm(forms.ModelForm):","    class Meta:","        model = Issue","        fields = ('title', 'description', 'image', 'tag', 'issue_type')","","","class CommentForm(forms.ModelForm):","    class Meta:","        model = Comment","        fields = ('comment',)"],"id":1}],[{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["y"],"id":2},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["l"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["p"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["e"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":["R"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":[" "]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"remove","lines":[","]}],[{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"remove","lines":["e"],"id":3},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"remove","lines":["l"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"remove","lines":["t"]},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"remove","lines":["i"]},{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"remove","lines":["t"]}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":["i"],"id":4},{"start":{"row":7,"column":20},"end":{"row":7,"column":21},"action":"insert","lines":["s"]},{"start":{"row":7,"column":21},"end":{"row":7,"column":22},"action":"insert","lines":["s"]},{"start":{"row":7,"column":22},"end":{"row":7,"column":23},"action":"insert","lines":["u"]},{"start":{"row":7,"column":23},"end":{"row":7,"column":24},"action":"insert","lines":["e"]},{"start":{"row":7,"column":24},"end":{"row":7,"column":25},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["n"],"id":5},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["a"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["m"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["i"],"id":6},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["s"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["u"],"id":7},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["e"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["_"]}],[{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["i"],"id":8},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["s"]},{"start":{"row":7,"column":56},"end":{"row":7,"column":57},"action":"insert","lines":["s"]},{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"insert","lines":["u"]},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["e"]},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["_"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":69},"end":{"row":7,"column":69},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564505174112,"hash":"d5b12509f14c19dda71516612054016c337bdaba"}