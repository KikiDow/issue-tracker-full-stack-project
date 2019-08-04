{"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":0,"column":0},"end":{"row":17,"column":133},"action":"insert","lines":["from django import forms","from .models import Order","","class MakePaymentForm(forms.Form):","    ","    MONTH_CHOICES = [(i, i) for i in range(1, 12+1)]","    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]","    ","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","    ","class OrderForm(forms.ModelForm):","    class Meta:","        model = Order","        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county')"],"id":1}],[{"start":{"row":17,"column":69},"end":{"row":17,"column":85},"action":"remove","lines":[" 'town_or_city',"],"id":2}],[{"start":{"row":17,"column":77},"end":{"row":17,"column":78},"action":"remove","lines":["_"],"id":3},{"start":{"row":17,"column":76},"end":{"row":17,"column":77},"action":"remove","lines":["t"]},{"start":{"row":17,"column":75},"end":{"row":17,"column":76},"action":"remove","lines":["e"]},{"start":{"row":17,"column":74},"end":{"row":17,"column":75},"action":"remove","lines":["e"]},{"start":{"row":17,"column":73},"end":{"row":17,"column":74},"action":"remove","lines":["r"]},{"start":{"row":17,"column":72},"end":{"row":17,"column":73},"action":"remove","lines":["t"]},{"start":{"row":17,"column":71},"end":{"row":17,"column":72},"action":"remove","lines":["s"]}],[{"start":{"row":17,"column":78},"end":{"row":17,"column":79},"action":"insert","lines":["_"],"id":4},{"start":{"row":17,"column":79},"end":{"row":17,"column":80},"action":"insert","lines":["l"]},{"start":{"row":17,"column":80},"end":{"row":17,"column":81},"action":"insert","lines":["i"]},{"start":{"row":17,"column":81},"end":{"row":17,"column":82},"action":"insert","lines":["n"]},{"start":{"row":17,"column":82},"end":{"row":17,"column":83},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":94},"end":{"row":17,"column":95},"action":"remove","lines":["_"],"id":5},{"start":{"row":17,"column":93},"end":{"row":17,"column":94},"action":"remove","lines":["t"]},{"start":{"row":17,"column":92},"end":{"row":17,"column":93},"action":"remove","lines":["e"]},{"start":{"row":17,"column":91},"end":{"row":17,"column":92},"action":"remove","lines":["e"]},{"start":{"row":17,"column":90},"end":{"row":17,"column":91},"action":"remove","lines":["r"]},{"start":{"row":17,"column":89},"end":{"row":17,"column":90},"action":"remove","lines":["t"]},{"start":{"row":17,"column":88},"end":{"row":17,"column":89},"action":"remove","lines":["s"]}],[{"start":{"row":17,"column":95},"end":{"row":17,"column":96},"action":"insert","lines":["_"],"id":6},{"start":{"row":17,"column":96},"end":{"row":17,"column":97},"action":"insert","lines":["l"]},{"start":{"row":17,"column":97},"end":{"row":17,"column":98},"action":"insert","lines":["i"]},{"start":{"row":17,"column":98},"end":{"row":17,"column":99},"action":"insert","lines":["n"]}],[{"start":{"row":17,"column":99},"end":{"row":17,"column":100},"action":"insert","lines":["e"],"id":7}],[{"start":{"row":17,"column":47},"end":{"row":17,"column":49},"action":"insert","lines":["''"],"id":8}],[{"start":{"row":17,"column":48},"end":{"row":17,"column":49},"action":"insert","lines":["e"],"id":9},{"start":{"row":17,"column":49},"end":{"row":17,"column":50},"action":"insert","lines":["m"]},{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["a"]}],[{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"remove","lines":["a"],"id":10}],[{"start":{"row":17,"column":50},"end":{"row":17,"column":51},"action":"insert","lines":["a"],"id":11},{"start":{"row":17,"column":51},"end":{"row":17,"column":52},"action":"insert","lines":["i"]},{"start":{"row":17,"column":52},"end":{"row":17,"column":53},"action":"insert","lines":["l"]}],[{"start":{"row":17,"column":54},"end":{"row":17,"column":55},"action":"insert","lines":[","],"id":12}],[{"start":{"row":17,"column":55},"end":{"row":17,"column":56},"action":"insert","lines":[" "],"id":13}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":122},"end":{"row":17,"column":122},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1564944673111,"hash":"7867da7e9f12c00ac27c66201a76bdc29ca61e89"}