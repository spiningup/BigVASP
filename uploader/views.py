from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import zipfile
import xml.etree.ElementTree as ET
from fractions import gcd
from uploader.models import Document#, Vaspkeys
from uploader.forms import DocumentForm
#from uploader.extract_vasp import extract_xml
from uploader.extract_vasp import int_names, float_names, string_names, logical_names, array_names, varray_names

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = request.FILES['docfile']
            if zipfile_is_valid(filename):
                fields = extract_xml(filename)
                newdoc = Document(docfile = filename, **fields)
                newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('uploader.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def zipfile_is_valid(filename):
    if zipfile.is_zipfile(filename):
        filehandler = zipfile.ZipFile(filename, 'r')
        archive = filehandler.namelist()
        if "vasprun.xml" in archive:
            return True
    return False
    

def extract_xml(filename):
    filehandler = zipfile.ZipFile(filename, 'r')
    vaspxml = filehandler.open('vasprun.xml', 'r')
    tree = ET.parse(vaspxml)
    root = tree.getroot()

    allnames = int_names + float_names + string_names + logical_names
    fields = {}
    for name in int_names:
        result = root.findall(".//*[@name='%s']"%(name))
        fields[name] = int(result[0].text)
    for name in float_names:
        result = root.findall(".//*[@name='%s']"%(name))
        fields[name] = float(result[0].text)
    for name in string_names:
        result = root.findall(".//*[@name='%s']"%(name))
        fields[name] = result[0].text
    for name in logical_names:
        result = root.findall(".//*[@name='%s']"%(name))
        txt = result[0].text.replace(' ', '')
        if txt == 'T':
            fields[name] = True
        elif txt == 'F':
            fields[name] = False

    # get chemical formula
    name = 'atomtypes'
    result = root.findall(".//*[@name='%s']"%(name))[0].getiterator('set')[0]

    formuladict = {}
    for item in result:
        atomname = item[1].text.replace(' ', '')
        natoms = int(item[0].text)
        formuladict[atomname] = natoms
    formulalist = sorted(formuladict.items(), key=lambda x: x[0])

    # get number of formula unit
    ncell = formulalist[0][1]
    if len(formulalist) > 1:
        for i in range(1, len(formulalist)):
            ncell = gcd(ncell, formulalist[i][1])

    formula = ""
    reducedformula = ""
    natoms = 0
    for i in formulalist:
        formula += i[0] + str(i[1])
        reducedformula += i[0] + str(i[1] / ncell)
        natoms += i[1]

    fields['natoms'] = natoms
    fields['ncell'] = ncell
    fields['reducedformula'] = reducedformula

    return fields
