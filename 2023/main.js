function generateColor() {
    return '#' + Math.floor(Math.random()*16777215).toString(16)
  }


function getJson(url) {
    return fetch(url)
        .then(result => result.json())
        .catch(error => {
            console.log(error);
        })
}


function mounted(array, ar, n) {
    this.getJson('./data.json')
        .then(data => {
            for (let el of data.articles) {
                array.push(el);
                ar.push(JSON.stringify(el));
            }
            n = data.clusters;
        });
 }

const articles = [];
const ar = [];
let number = 5;
mounted(articles, ar, number);
setTimeout(() => {console.log(number);}, 1000)

let dataX = [];
let dataY = [];
let dataClass = [];
setTimeout(() => {
    for (let i of articles) {
        dataX.push(i.axisX);
        dataY.push(i.axisY);
        dataClass.push(i.class);     
    }
    
  }, 1000);
  

setTimeout(() => {
    console.log(articles[0].class);
    let linkData = []; let nameData = [];
    for (let i = 0; i < dataX.length; i++) {
        linkData.push(articles[i].doi);
        //nameData.push(articles[i].title);
        nameData.push(i + 1);
    }
 
    let colorNumber = [];
    for (let i = 0; i < number; i++) {
        colorNumber.push(generateColor());
    }

    let colorData = [];
    for (let i = 0; i < dataX.length; i++) {
        console.log(articles[i].class);
        if (articles[i].class == 0) {
            colorData.push('red');
        }
        else if (articles[i].class == 1) {
            colorData.push('green');
        }
        else if (articles[i].class == 2) {
            colorData.push('yellow');
        }
        else if (articles[i].class == 3) {
            colorData.push('blue');
        }
        else if (articles[i].class == 4) {
            colorData.push('purple');
        }
        else if (articles[i].class == 5) {
            colorData.push('orange');
        }
        else if (articles[i].class == 6) {
            colorData.push('pink');
        }
        //colorData.push(colorNumber[articles[i].class]);
    }
    console.log(colorData);

    var trace1 = {
        x: dataX,
        y: dataY,
        mode: 'markers+text',
        textposition: 'top center',
        textsize: 6,
        text: nameData,
        marker: {
          size: 10,
          color: colorData
        },
        name: 'Classes'
    };
    var data = [trace1];
  
    var layout = {
        title: 'Clusterization',
        showlegend: false,
        height: 800,
        width: 800,
        legend: {
            y: 0.5,
            yref: 'paper',
            font: {
              family: 'Arial, sans-serif',
              size: 20,
              color: 'grey',
            }
        }
    };
  
    const myPlot = document.getElementById('myDiv');
    Plotly.newPlot(myPlot, data, layout);

    myPlot.on('plotly_click', function(data){
        if (data.points.length === 1) {
          let link = linkData[data.points[0].pointNumber];
          console.log(linkData[data.points[0].pointNumber]);
          // Note: window navigation here.
          window.open(link);
        }
      });
  }, 5000);


  
  
  

  

