from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.http import Http404
import logging
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
logger = logging.getLogger(__name__)

import csv
from webapp.models import ThreeOneOneData, CommunityName
import simplejson as json

@csrf_exempt
def home(request):
	populate()
	community_board_list = sorted(list(CommunityName.objects.all()))
	return render_to_response('base.html', RequestContext(request, locals()))

@csrf_exempt
def community(request):
	if 'cancel' in request.POST and request.POST['cancel']:
		logger.info('Cancelled Request')
		return redirect('/home')
	if 'Comunity Names' in request.POST and request.POST['Comunity Names']:
		name = request.POST['Comunity Names']
		logger.debug('Name = ' + name)
		try:
			community = ThreeOneOneData.objects.get(name = name)
			return render_to_response('community.html', RequestContext(request, locals()))
		except Exception:
			logger.error('Exception getting data from database')
	return redirect('/home')


def populate():
	if ThreeOneOneData.objects.count() > 0:
		return
	
	reader = csv.DictReader(open('311data.csv', 'rU'))	
	
	community_data = dict()
	
	for row in reader:
		key = 'Community Board'
		print 'P1 - ' + row[key]
		if row[key] not in community_data:
			community_data[row[key]] = list()
		community_data[row[key]].append(row)
		# community_entry = CommunityName(name = row[key])
		# community_entry.save()	
	print 'community count = ' + str(len(community_data))

	overall_summary = dict()

	for community_name in community_data.keys():
		community_summary = dict()
		community_summary['count'] = len(community_data[community_name])
		print 'Name = ' + community_name + ' Count = ' + str(community_summary['count'])
		key = 'Complaint Type'
		for count in range(len(community_data[community_name])):
			individual_complaint = community_data[community_name][count]
			if individual_complaint[key] not in community_summary:
				community_summary[individual_complaint[key]] = {'count':0}
			community_summary[individual_complaint[key]]['count'] += 1
		print 'Done for ' + community_name
		
		d3_list = list()
		for complaint in community_summary.keys():
			if complaint != 'count':
				d3_list.append({'complaint':complaint, 'count':community_summary[complaint]['count']})

		overall_summary[community_name] = community_summary
		overall_summary[community_name]['d3'] = d3_list
		
	
	for community_name in overall_summary.keys():
		try:
			threeoneone_database_entry = ThreeOneOneData(
											name = community_name,
											count = overall_summary[community_name]['count'],
											json_data = json.dumps(overall_summary[community_name]['d3']))
			threeoneone_database_entry.save()
			community_name_entry = CommunityName(name = community_name)
			community_name_entry.save()
		except Exception:
			logger.error('Caught some Exception adding data to the database')


