document.addEventListener("DOMContentLoaded", function(event) {
    console.log("DOM fully loaded and parsed");
    //Your code to bind event handler
    console.log('page load - entered main.js for js-other api');

    var modifyPokemonButton = document.getElementById('modifyPokemonButton');
    modifyPokemonButton.onmouseup = modifyPokemonInfo;
    }
);


// functions for get a pokemon
function modifyPokemonInfo(){
    console.log('entered get pokemon info');
    var pokemonName = document.getElementById("nameInputModify").value;
  	if (pokemonName != "") {
    	makeModifyNetworkCallToPokemonApi(pokemonName);
    }
} // end of getFormInfo

function makeModifyNetworkCallToPokemonApi(pokemonName){
    console.log('entered makeGetNetworkCallToPokemonApi');
    var url = "http://localhost:51055/pokemon/" + pokemonName;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("PUT", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e){
        console.log('network response received' + xhr.responseText);
        // do something
        updatePokemonWithResponse(pokemonName, xhr.responseText);
    } // end of onload

    // set up onerror - triggered if n response is error response
    xhr.onerror = function(e){
        console.error(xhr.statusText);
    } // end of onerror
    var types = document.getElementById('typeInputModify').value;
    var stats = document.getElementById('statsInputModify').value;
    var imageUrl = document.getElementById('imageInputModify').value;
    pokemonName = String(pokemonName);
    var data = '{"name" : "' + pokemonName + '","types" : "' + types + '","base" : "' + stats + '","image" : "' + imageUrl + '"}';
    var data2 = '{"name":"bulbasaur", "types":"Im tired", "image": "hello", "base":"???"}';
    console.log("the data2 from modify is: " + data2);
    console.log("the data from modify is:" + data);
    xhr.send(data); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updatePokemonWithResponse(pokemonName, response_text){
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
    var name = document.getElementById('nameInputModify');
    var types = document.getElementById('typeInputModify');
    var stats = document.getElementById('statsInputModify');
    var url = document.getElementById('imageInputModify')

    if((response_json['name'] == null) || (response_json['types'] == null) || (response_json['stats'] == null) || (response_json['image'] == null)){
        displayName.innerHTML = 'Apologies, we could not find your pokemon info.';
        displayType.innerHTML = ' ';
      	displayStats.innerHTML = ' ';
    } else if (response_json['message'] == 'pokemon not found') {
		displayName.innerHTML = 'Apologies, we could not find your pokemon info. 2';
      	displayType.innerHTML = ' ';
      	displayStats.innerHTML = ' ';
    }
               
  	else{
        displayName.innerHTML = "Name" + name
      	displayType.innerHTML = "Type" + type
        displayStats.innerHTML = "Stats" + stats
      	imageURL = url;
        // var names = document.getElementsByClassName('name-list');
        // while(names[0]) {
        //     names[0].parentNode.removeChild(names[0]);
        // }​
      	displayImage.src = imageURL;
    }

} // end of updateAgeWithResponse
