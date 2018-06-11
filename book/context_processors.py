from .models import Year


def sems(request):	
	year1_sems = Year.objects.get(name=1).sems.all()
	year2_sems = Year.objects.get(name=2).sems.all()
	year3_sems = Year.objects.get(name=3).sems.all()
	year4_sems = Year.objects.get(name=4).sems.all()	
	return {"year1_sems":year1_sems,
			"year2_sems":year2_sems,
			 "year3_sems":year3_sems,
			 "year4_sems":year4_sems}  
	# return {"c":'c'}

