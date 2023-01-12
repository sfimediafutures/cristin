# cristin

by Koenraad De Smedt, University of Bergen

A small Python program that uses the API to CRISTIN for accessing
results linked to projects.
This is useful if you want to keep track of the results that will
appear automatically in the yearly project reporting, which of
course uses the same API. 

The CRISTIN API is described here: [https://www.cristin.no/tjenester/api/]

The Python program does not have the overview of all project
names and codes, but keeps the relation for some project names and
codes in a dict, which can of course be extended.

When the program is executed, the following code prints
summary information about each result for MediaFutures:

```print_project_results('MediaFutures’)```

Currently, the summary information that is printed about each
result is limited.
Clearly, you could extend the program to filter certain types
of results, or you could format the results in different ways,
but that is left as homework :)

The following makes a bar chart for the number of results per year:

```plot_project_results('MediaFutures’)```

You can use this to compare the numbers over the years.
