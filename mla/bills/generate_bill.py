 
# 

def get_genearate_bill(req):

		range_start = 10**(8-1)
		range_end = (10**8)-1
		generated_rand_num =  randint(range_start, range_end)
		refno = "BRN"+str(generated_rand_num)
 

	form = TINForm(req.POST)

	if form.is_valid():
	
		try:	 
		# today = date.today()
		 

		 tin = form.cleaned_data.get('tin')
		 
		 name =form.cleaned_data.get('name')
		 mda = form.cleaned_data.get('mda')
		 revenuitem = form.cleaned_data.get('revenuitem')
		 period = form.cleaned_data.get('period')
		 amount = form.cleaned_data.get('amount')

		 MDA_bill.objects.create(tdate, refno, tin, name, mda, revenue_item, period, amount, status) VALUES (' date',' refno',' tin',' name',' mda',' revenuitem',' period',' amount','notpaid')";
 		
 		 mda_ebills = mda_ebills.obj.filter(tin =bill_tin,  status ='notpaid',  refno = bill_refno)

 
		return render(req, 'bill.html', {'date, tin, name, mda, revenuitem, period, amount', "mda_ebills":mda_ebills})

	except as e:
		print(e)


  