#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Find project results with the CRISTIN API

import requests

# a few project codes
project_dict = {'MediaFutures':'309339', 'CLARINO+':'295700',
                'CLARINO':'208375', 'INESS':'195323'}

cristin_fundings_url = 'https://api.cristin.no/v2/fundings'

def find_funding_url (source, project_name):
  project_code = project_dict[project_name]
  response = requests.get(cristin_fundings_url,
                          params={'funding_source':source,
                                  'project_code':project_code})
  if response.status_code == 200:
    data = response.json()
    #print(data)
    return data[0]['url']
  else:
    print('Not a valid request')
    
find_funding_url('NFR', 'MediaFutures') # MediaFutures
# https://api.cristin.no/v2/fundings?funding_source=NFR&project_code=309339

def print_project_results (project_name, source='NFR'):
  url = find_funding_url(source, project_name)
  response = requests.get(url+'/results') #, verify=False
  if response.status_code == 200:
    data = response.json()
    #print(data)
    for result in data:
      print_project_result(result)
    #return data
  else:
    print('Not a valid request')

def print_project_result (result):
  for t in result['title']:
    print(result['title'][t])
  print(f"   ({result['category']['name']['en']} {result['year_published']})")
  #print(result['contributors'])
  for contributor in result['contributors']['preview']:
    print('  ', contributor['first_name'], contributor['surname'])
  if result['contributors']['count'] > len(result['contributors']['preview']):
    print('      et al.')

print_project_results('MediaFutures')
#print_project_results('CLARINO+')

from collections import Counter
import matplotlib.pyplot as plt

def plot_project_results (project_name, source='NFR'):
  url = find_funding_url(source, project_name)
  response = requests.get(url+'/results')
  if response.status_code == 200:
    data = response.json()
    #print(data)
    years = Counter([result['year_published'] for result in data])
    plt.figure(dpi=120)
    plt.bar(years.keys(),[years[i] for i in years])
    #plt.yscale('log')
    plt.title('Project results '+project_name)
    plt.ylabel('Number of results')
    plt.xlabel('Years')
    plt.show()
    #return data
  else:
    print('Not a valid request')

# Note that project results already seem to be sorted

plot_project_results('MediaFutures')
#plot_project_results('CLARINO+')
