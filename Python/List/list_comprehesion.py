#expression
# [expression for item in iterable if condition ]
org = ["IT","Non-It","banking","technical"]

new_org = [ y_ for y_ in org if "I" in y_]

print(new_org)