# import mymodule as MM
# from mymodule import find_index, test
# from mymodule import * # should not import star. may overwrite local stuff

import sys
from subdir import subdirmodule as SDM


courses = ['History', 'Math', 'Physics', 'CompSci']
index = SDM.find_index(courses, 'Math')
# print(index)
# print(test)


# print(sys.path)