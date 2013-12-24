# -*- coding: utf-8 -*-
#/usr/bin/python
# LGPL2
# made by tkrasuski@gazete.pl
import numbers
import decimal

# exceptions

class pyXchartsEception(Exception):
    pass

class wrongScaleException(pyXchartsEception):
    pass

class wrongValue(pyXchartsEception):
    pass

class wrongChartType(pyXchartsEception):
    pass

class noData(pyXchartsEception):
    pass



# chart objects

class chart(object):
    name = 'myChart'
    cname = 'myCompChart'
    xScale = 'ordinal'
    yScale = 'ordinal'
    xMin = None
    xMax = None
    yMin = None
    yMax = None
    chartType = 'bar'
    cChartType = 'line'
    figure = ''
    # private fields
    __data = ''
    __compdata = ''
    
    __shell = """
    {
      "xScale": "%s",
      "yScale": "%s",
      "type": "%s",
      "%s": [
        {
          "className": ".%s",
          %s
        }
      ]
    """
    
    __compshell = """
    ,
     "comp": [
    {
      "className": ".%s",
      "type": "%s",
      "data": [
        %s
      ]
    }
  ]
}
    """
    
    __datatmp = """
    "data": [
            %s
            ]
    """
    
    __dataItemtmp = """
            {
              "x": "%s",
              "y": %s
            }
    """
    def validate(self):
        if self.xScale not in ('ordinal','linear','time','exponential'):
            raise wrongScaleException('Wrong scale.')
        if not isinstance(self.xMin,numbers.Number) and self.xMin!=None:
            raise wrongValue('xMin must be a number.')
        if not isinstance(self.xMax ,numbers.Number) and self.xMax !=None:
            raise wrongValue('xMax must be a number.')
        if not isinstance(self.yMax ,numbers.Number) and self.yMax !=None:
            raise wrongValue('yMax must be a number.')
        if not isinstance(self.yMin ,numbers.Number) and self.xMin !=None:
            raise wrongValue('xMin must be a number.')
        if self.chartType not in ('bar','line','line-dotted','cumulative'):
            raise wrongChartType('Use valid chart type.')
    
    def addItem(self, data):
        dataItem = self.__dataItemtmp % (data['x'], data['y'])
        if len(self.__data)>0:
            self.__data += '\n , \n'
        self.__data += dataItem
    
    def addCompItem(self, data):
        dataItem = self.__dataItemtmp % (data['x'], data['y'])
        if len(self.__compdata)>0:
            self.__compdata += '\n , \n'
        self.__compdata += dataItem
        
    def addItems(self, data):
        if len(data)!=0:
            for d in data:
                self.addItem(d)
            
    
        
    def create(self):
        self.validate()
        dat = self.__datatmp % self.__data
        she = self.__shell % (self.xScale, self.yScale, self.chartType, 'main', self.name, dat)
        if len(self.__compdata)>0:
            shc = self.__compshell % (self.cname, self.cChartType , self.__compdata)
            self.figure=she+shc
        else:
            self.figure = she+'}'
    def getChart(self):
        return self.figure
    
    def getAsFunction(self):
        ret = 'new xChart(\'%s\', %s , \'#%s\')' %(self.chartType,self.figure,self.name)
        return ret
    
    def getAsScript(self):
        ret = '<script> %s ;</script>' % self.getAsFunction()
        return ret
    
    def clearData(self):
        self.__data=None
        
    def clearCompData(self):
        self.__compdata=None
    
    
    







