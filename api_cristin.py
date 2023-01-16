#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Find project results with the CRISTIN API
# by Koenraad De Smedt

import requests

# a few project codes at some sources, add more if needed
project_dict = {'NFR':{'MediaFutures':'309339', 'CLARINO+':'295700',
                       'CLARINO':'208375', 'INESS':'195323',
                       'LIA':'225941'},
                'SIGMA2':{'Fillagring':'NS9691K'}}

cristin_fundings_url = 'https://api.cristin.no/v2/fundings'

def find_funding_url (source, project_name):
  project_code = project_dict[source][project_name]
  response = requests.get(cristin_fundings_url,
                          params={'funding_source':source,
                                  'project_code':project_code})
  if response.status_code == 200:
    data = response.json()
    # print(data)
    if data != []: 
      return data[0]['url']
  else:
    print('Not a valid request')
    
find_funding_url('NFR', 'MediaFutures')
find_funding_url('NFR', 'CLARINO+')
find_funding_url('SIGMA2', 'Fillagring')

# https://api.cristin.no/v2/fundings?funding_source=NFR&project_code=309339

def print_project_results (project_name, source='NFR'):
  url = find_funding_url(source, project_name)
  if url:
    response = requests.get(url+'/results') #, verify=False
    if response.status_code == 200:
      data = response.json()
      #print(data)
      for result in data:
        print_project_result(result)
      return len(data)
    else:
      print('Not a valid request')

def print_project_result (result):
  for t in result['title']:
    print(result['title'][t])
  print(f"   ({result['year_published']}) -- {result['category']['name']['en']}")
  print_contributors(result['contributors']['preview'],
                     result['contributors']['count'])

# this version prints authors on one line
def print_contributors (contributors, count):
  nameslist = [c['first_name'] + ' ' + c['surname'] for c in contributors]
  namestring = '   ' + ', '.join(nameslist)
  if count > len(contributors):
    namestring = namestring + ', et al.'
  print(namestring)

# this version prints contributors on separate lines
def print_contributors (contributors, count):
  for contributor in contributors:
    print('  ', contributor['first_name'], contributor['surname'])
  if count > len(contributors):
    print('      et al.')
  for t in result['title']:
    print(result['title'][t])
  print(f"   ({result['year_published']}) -- {result['category']['name']['en']}")
  #print(result['contributors'])
  for contributor in result['contributors']['preview']:
    print('  ', contributor['first_name'], contributor['surname'])
  if result['contributors']['count'] > len(result['contributors']['preview']):
    print('      et al.')

print_project_results('MediaFutures')
print_project_results('CLARINO+')
print_project_results('Fillagring', 'SIGMA2')

from collections import Counter
import matplotlib.pyplot as plt

def plot_project_results (project_name, source='NFR'):
  url = find_funding_url(source, project_name)
  if url:
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
      return years
    else:
      print('Not a valid request')

# Note that project results already seem to be sorted

plot_project_results('MediaFutures')
plot_project_results('CLARINO+')
plot_project_results('Fillagring', 'SIGMA2')
