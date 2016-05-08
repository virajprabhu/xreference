from django.shortcuts import get_object_or_404, render
from .models import Publication

# Create your views here.
def index(request):
	context = {}
	if request.method == "POST":
		# TODO: perform validation here
		# try:
		# 	
		# except (KeyError):
		# 	# throw exceptions here
		# else:
		# 	# create publication and save, display success
		# 	# and redirect to home page


		if 'title' in request.POST:
			# Add request
			file_url = request.POST['file_url']
			title = request.POST['title']
			author = request.POST['author']
			keywords = request.POST['keywords']
			year = request.POST['year']
			venue = request.POST['venue']
			pub = Publication(title=title, author=author,
							 keywords=keywords, year=year,
							 venue=venue, file_url=file_url)
			pub.save()
		else:
			# Query request
			query_string = request.POST['search']

			qres_title = Publication.objects.filter(title__icontains=query_string)
			qres_author = Publication.objects.filter(author__icontains=query_string)
			qres_keywords = Publication.objects.filter(keywords__icontains=query_string)
			qres_venue = Publication.objects.filter(venue__icontains=query_string)
			qres_year = Publication.objects.filter(year__icontains=query_string)

			query_results = qres_title | qres_author | qres_year | qres_venue | qres_keywords
			print(query_results)
			context = {'query_results': query_results}

	return render(request, 'core/index.html', context)