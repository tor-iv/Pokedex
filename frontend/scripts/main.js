console.log('page load - entered main.js for js-other api');

var submitButton = document.getElementById('submit-button');
submitButton.onmouseup = getFormInfo;

function getFormInfo(){
    console.log('entered get form info');
    var zip = document.getElementById("input-text-zip").value;
    makeNetworkCallToZipApi(zip);
} // end of getFormInfo

function makeNetworkCallToZipApi(zip){
    console.log('entered makeNetworkCallToZipApi');
    var url = "https://api.zippopotam.us/us/" + zip;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("GET", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e){
        console.log('network response received' + xhr.responseText);
        // do something
        updateWeatherWithResponse(zip, xhr.responseText);
    } // end of onload

    // set up onerror - triggered if nw response is error response
    xhr.onerror = function(e){
        console.error(xhr.statusText);
    } // end of onerror

    xhr.send(null); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updateWeatherWithResponse(zip, response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
    var label1 = document.getElementById('response-line1');
  	var label2 = document.getElementById('response-line2');
    var label3 = document.getElementById('response-line3');


    if((response_json['places'][0]['longitude'] == null) || (response_json['places'][0]['latitude'] == null)){
        label1.innerHTML = 'Apologies, we could not find your zip info.';
    } else{
        label1.innerHTML = 'Longitude = ' + response_json['places'][0]['longitude'];
      	label2.innerHTML = 'Latitude = '  + response_json['places'][0]['latitude'];
        label3.innerHTML = response_json['places'][0]['place name'] +
        ', ' + response_json['places'][0]['state abbreviation'];
        // make nw call to number api
        var long = parseInt(response_json['places'][0]['longitude']);
      	var lat = parseInt(response_json['places'][0]['latitude']);
        makeNetworkCallToWeatherApi(long, lat);
    }

} // end of updateAgeWithResponse

function makeNetworkCallToWeatherApi(long, lat){
    console.log('enetered makeNetworkCallToWeatherApi');
    var url = "http://www.7timer.info/bin/astro.php?lon="+long+"&lat="+lat+"&ac=0&lang=en&unit=metric&output=internal&tzshift=0";
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);

    xhr.onload = function(e) {
        console.log('got nw response from weatherapi');
        updateTriviaWithResponse(url);
    }

    xhr.onerror = function(e){
        console.error(xhr.statusText);
    }

    xhr.send(null); // send request without bosy
} // end of makeNetworkCallToNumbersApi

function updateTriviaWithResponse(url){
    console.log('enetered updateTriviaWithResponse');
    var label2 = document.getElementById("response-line2");
//    label2.innerHTML = response_text;

    // dynamically adding a label

  	var img = document.createElement('img');
    img.src = url;
    var container = document.getElementById('response').appendChild(img);


} // end of updateTriviaWithResponse
