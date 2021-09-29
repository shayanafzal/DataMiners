function init() {
    // Use the list of sample names to populate the select options
   data = d3.json("data.json").then((data) => {
    var year = data.map(year => parseInt(year.YEAR_))
    console.log(year)
    var flavour = data.map(flavour => flavour.Flavours)
    console.log(flavour)
    var value = data.map(value => parseInt(value.CAD_Value))
    console.log(value)
    var place = data.map(place => place.Market)
    console.log(place)
    var health = data.map(health => health.SubCategory)
    console.log(health)
    var listOfPlaces =[]

    var trace = {
      x: flavour,
      y: value,
      type: "bar"
    };
    var data = [trace];
    var layout = {
      title: "Snack Bars Sales by Flavour",
      xaxis: { title: "Flavours" },
      yaxis: { title: "CAD_Value"}
    };
    Plotly.newPlot("bar-plot", data, layout);

    var trace = {
      labels: place,
      values: value,
      type: 'pie'
     };
     var data = [trace];
     var layout = {
      title: "Snack Bars Sales by Location",
     };
     Plotly.newPlot("plotArea", data, layout);
     
    var trace = {
      x: year,
      y: value,
      z: flavour,
      mode: 'markers',
      type: 'scatter'
    };
     var data = [trace];
     var layout = {
      title: 'Snack Bars Sales by Year'
    };
    
    Plotly.newPlot('myDiv', data, layout);

    var trace = {
      x: health,
      y: value,
      type: "bar"
    };
    var data = [trace];
    var layout = {
      title: "Snack Bars Sales by Health Category",
      xaxis: { title: "Health Category" },
      yaxis: { title: "CAD_Value"}
    };
    Plotly.newPlot("bar-plot-health", data, layout);
    })
  }

init();

function pred() {
  pred = d3.json("predictions.json").then((pred) => {
    console.log(pred);
    var date = pred.map(date => (date.ds));
    console.log(date);
    var sales = pred.map(sales => parseInt(sales.yhat));
    console.log(sales);

// line graph of predictive model 
    var trace = {
      x: date,
      y: sales,
      type: 'line'
    };
     var data = [trace];
     var layout = {
      title: 'Predicted Snack Bars Sales by Year'
    };
    
    Plotly.newPlot('myDiv_pred', data, layout);
  });
}
pred();
  



  
  