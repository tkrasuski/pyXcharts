## pyXcharts - pythonic wraper to the Xcharts

Xcharts is a java script library to creating charts for your web page. It is really simple and handy, however mixing java script, jQuery and python is not very pleasant.
So, if you're writing python web application and you like Xcharts  you can make your work much easier using pyXchart.

### Before you start

Before you start, you need add some additional libraries for your project:
* Download and include [D3.js](http://d3js.org/) on your page (Xcharts uses it).
* Download and include [xcharts.js and xcharts.css](http://tenxer.github.io/xcharts/) on your page.
* Download [pyXcharts](https://github.com/tkrasuski/pyXcharts) and place in accessible folder.

### My first chart

Ok, looks like we're ready. Let's create our first chart. With your favorit editor create script including code below.


    import pyxchart as px

    chart = px.chart() # creates instance of chart object
    a = {'x':'Cola','y':30} # first data series
    b = {'x':'Beer','y':70} # second data series
    chart.addItem(a) # adding first data series to the chart
    chart.addItem(b)
    chart.name='Drinks' # name for report and HTML class ID
    chart.create() # generate chart
    chartFigure = chart.getAsFunction() # contains chart code for use in the view file

Now, depending on framework you using, you should place some code in the view file. This example shows how to use pyXcharts with the web2py framework.

Your controler file:
    
    import pyxchart as px
    def index():
    	chart = px.chart() # creates instance of chart object
    	a = {'x':'Cola','y':30} # first data series
    	b = {'x':'Beer','y':70} # second data series
    	chart.addItem(a) # adding first data series to the chart
    	chart.addItem(b)
    	chart.name='Drinks' # name for report and HTML class ID
    	chart.create() # generate chart
    	chartFigure = chart.getAsFunction()
    return dict(msg=XML(chartFigure))

Your view file:

    <figure style="width: 400px; height: 300px;" id="Drinks"></figure>
    <script> {{=msg}} ;</script>

For more details about how to use pyXcharts with web2py take a look at "web2py how to"
