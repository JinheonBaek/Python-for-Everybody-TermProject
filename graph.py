import matplotlib.pyplot as plt
import mpld3, math, myutil

class Graph():
    def __init__(self, name, function, xmin=-3, xmax=3):
        self._name = name
        self._function = function
        self._xmin = xmin
        self._xmax = xmax

    def get_name(self):
        return self._name

    def get_xmin(self):
        return self._xmin

    def get_xmax(self):
        return self._xmax

    def get_function(self):
        return self._function

def draw(graphLst, funDatas):
    fig = plt.figure(0)
    fig.clf()

    #Draw Graph
    for i in range(len(graphLst)):
        t = range(int(graphLst[i].get_xmin())*100, int(graphLst[i].get_xmax())*100)
        x = [t/100 for t in t]
        y = [graphLst[i].get_function()(x) for x in x]
        plt.plot(x, y)
    
    #Using legend
    funLst = []
    for i in range(len(funDatas)):
        funLst.append('y' + str(i) + ' : ' + funDatas[i])
    plt.legend(funLst, loc='upper left')

    html = mpld3.fig_to_html(fig)

    return html

def getSample():
    graphLst = [Graph('y1', lambda x: x), Graph('y2', lambda x: 2*x-3), Graph('y3', lambda x: x*x-10)]
    return graphLst

def getGraphList(data):
    graphLst = []
    for i in range(len(data['name'])):
        ldict = locals()
        exec(data['function'][i], globals(), ldict)
        f = ldict['f']
        graphLst.append(Graph(data['name'][i], f, data['xmin'][i], data['xmax'][i]))
    return graphLst