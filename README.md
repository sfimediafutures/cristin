# cristin

A small Python program that uses the API to CRISTIN for accessing
results linked to certain RCN projects.
This is useful if you want to keep track of the results that will
appear automatically in the yearly project reports, which of
course uses the same API.

When the program is executed, the following prints summary
information about each result for MediaFutures:

```print_project_results('MediaFutures’)```

Clearly, you could extend the program to filter certain types
of results, or you could format the results in different ways,
but that is left as homework :)

The following makes a bar chart for the number of results per year:

```plot_project_results('MediaFutures’)```

You can use this to compare the numbers over the years.
