{
  "title": "Linecount",
  "date": "2014-01-15",
  "categories": [
    
  ],
  "tags": [
    
  ]
}


<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>
      Google Visualization API Sample
    </title>
    <script type="text/javascript" src="//www.google.com/jsapi"></script>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.1.min.js"></script>

    <script type="text/javascript">
      google.load('visualization', '1', {packages: ['annotatedtimeline']});
    </script>
    <script type="text/javascript">
      function drawVisualization() {
        // Create and populate the data table.
        var jsonData;
        $.ajax({
        url: "assets/media/linecount.json",
        async: false,
        dataType: 'json',
        success: function(data) {
          jsonData= data;
        }
      });
        var data = new google.visualization.DataTable(jsonData, 0.5);
       // Create and draw the visualization.
        var timeline = new google.visualization.AnnotatedTimeLine(document.getElementById('visualization'));
        timeline.draw(data, {'displayAnnotations': true});

        var jsonData2;
        $.ajax({
        url: "assets/media/daily.json",
        async: false,
        dataType: 'json',
        success: function(data) {
          jsonData2= data;
        }
      });
        var data = new google.visualization.DataTable(jsonData2, 0.5);
       // Create and draw the visualization.
        var timeline = new google.visualization.AnnotatedTimeLine(document.getElementById('daily'));
        timeline.draw(data, {'displayAnnotations': true});
      }
      google.setOnLoadCallback(drawVisualization);
    </script>
  </head>
  <body style="font-family: Arial;border: 0 none;">

<h2>Daily Progress for the past 30 days</h2>
    <div id="daily" style="width: 500px; height: 400px;"></div>
<h2>Overall overview</h2>
    <div id="visualization" style="width: 500px; height: 400px;"></div>
  </body>
</html>
