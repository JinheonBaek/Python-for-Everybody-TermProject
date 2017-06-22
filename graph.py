import matplotlib.pyplot as plt
import mpld3, math, myutil
import solve
from exception import MyException

class Graph():
    def __init__(self, name, function, xmin=-5, xmax=5, solution = [], error=1E-9):
        self._name = name
        self._function = function
        self._xmin = xmin
        self._xmax = xmax
        self._solution = solution
        self._error = error

    def get_name(self):
        return self._name

    def get_xmin(self):
        return self._xmin

    def get_xmax(self):
        return self._xmax

    def get_function(self):
        return self._function

    def get_solution(self):
        return self._solution

    def get_error(self):
        return self._error

def draw(graphLst, funDatas, isSolve=True):
    fig = plt.figure(0)
    fig.clf()

    #Draw Graph
    for i in range(len(graphLst)):
        t = range(int(graphLst[i].get_xmin())*100, int(graphLst[i].get_xmax())*100)
        x = [t/100 for t in t]
        y = [graphLst[i].get_function()(x) for x in x]
        plt.plot(x, y)

    #Find Solution
    if isSolve is not False:
        for i in range(len(graphLst)):
            t = range(int(graphLst[i].get_xmin())*100, int(graphLst[i].get_xmax())*100)
            x = [t/100 for t in t]
            y = [0 for y in x]

            for j in graphLst[i].get_solution():
                plt.plot(x, y)
                plt.plot(j, 0, 'bo')

    #Using legend
    funLst = []
    for i in range(len(funDatas)):
        funLst.append('y' + str(i+1) + ' : ' + funDatas[i])

    plt.legend(funLst, loc='upper left')

    html = mpld3.fig_to_html(fig)

    return html

def getSample():
    graphLst = [Graph('y1', lambda x: x-1, solution=[1.00000000076294]), Graph('y2', lambda x: x*x-3, solution=[-1.7320508073806766, 1.7320508073806762]), Graph('y3', lambda x: math.sin(3*x), solution=[-2.09439510269165, -1.047197551345825, 1.047197551345825, 2.0943951026916507])]
    return graphLst

def getGraphList(data):
    graphLst = []
    for i in range(len(data['name'])):
        if data['function'][i].find('f') < 0:
            raise MyException("Some function form have some error ex) f = lambda x: x-1")
        ldict = locals()
        exec(str(data['function'][i]), globals(), ldict)
        f = ldict['f']
        graphLst.append(Graph(data['name'][i], f, data['xmin'][i], data['xmax'][i], solve.solution_finder(f, float(data['xmin'][i]), float(data['xmax'][i]))))

    return graphLst
