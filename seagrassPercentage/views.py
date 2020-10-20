import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from subprocess import Popen, PIPE, STDOUT
from seagrassPercentage.models import User, Picture

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# Create your views here.
def Form(request):
	form = None
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			myfile = request.FILES['file']
			#upload images to database
			richard = User.objects.get(pk=1)
			pic = Picture(user=richard,image=myfile,processedimage=myfile)
			pic.save()
			path = pic.processedimage.path		
			#fs = FileSystemStorage()
			#filename = fs.save(myfile.name, myfile)
			#uploaded_file_url = fs.url(filename)
			# call your python code for image processing
			#print('processing', uploaded_file_url)
			print('processing', path)
			process = Popen(["python3","/Users/richard/aglantisWebsite/seagrassPercentage/imgproc/seagrassCounter.py","-i",path])
			#command = 'python /Users/richard/aglantisWebsite/seagrassPercentage/imgproc/seagrassCounter.py -i' + path
			#os.system(command)
			return HttpResponse("File(s) uploaded!")
		else:
			print('form invalid')
			form = UploadFileForm()
            
	return render(request, "seagrassPercentage/index.html",  {'form': form})
