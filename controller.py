from tornado.web import RequestHandler
import graph

import matplotlib.pyplot as plt
import mpld3, math

class MainHandler(RequestHandler):
    def get(self):
        graphLst = graph.getSample()
        data = {'name': ['y1', 'y2', 'y3'], 'function': ["f = lambda x: x-1", "f = lambda x: x*x-3", "f = lambda x: math.sin(3*x)"], 'xmin': [-3, -3, -3], 'xmax': [3, 3, 3], 'length': 3}

        self.render('index.html', graph=graph.draw(graphLst, data['function']), data=data, graphLst=graphLst)

    def post(self):
        data = {'name': [], 'function': [], 'xmin': [], 'xmax': [], 'length': 0}

        for i in range(9):
            if len(self.get_body_argument('y' + str(i+1) + '_function')) > 0:
                data['length'] += 1
                data['name'].append('y' + str(i+1))
                data['function'].append(self.get_body_argument('y' + str(i+1) + '_function'))
                data['xmin'].append(self.get_body_argument('y' + str(i+1) + '_xmin'))
                data['xmax'].append(self.get_body_argument('y' + str(i+1) + '_xmax'))

        graphLst = graph.getGraphList(data)
        try:
           self.render('index.html', graph=graph.draw(graphLst, data['function']), data=data, graphLst=graphLst)
        except Exception:
           self.render('error.html')
