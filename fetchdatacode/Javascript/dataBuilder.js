var dataBuilder = (function() {

	var body = document.body;

	/* Global datasets */
	var categorySpeciesArray = {};
	var speciesThreatsArray = {};
	var speciesThreatsObject = {};
	var speciesIdArray = [];
	var asyncCount = 0;
	var asyncLimit = 0;
	var rateLimit = 500;

	var getSpeciesIdByCategory = function(category) {
		// To refer, look at "http://apiv3.iucnredlist.org/api/v3/species/category/VU?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee"
		httpGet('http://apiv3.iucnredlist.org/api/v3/species/category/'+category+'?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee',function() {
			var response = JSON.parse(event.target.response);
			categorySpeciesArray[category] = response;
			var speciesSubArray = response.result;
			speciesIdArray = [];
			// Build an array of only the IDs of species we want
			for (var i = 0; i < speciesSubArray.length; i++) {
				speciesIdArray.push(speciesSubArray[i]["taxonid"])
			}
			asyncCount = 0;
			asyncLimit = speciesIdArray.length;
			buildSpeciesThreats(speciesIdArray,0);
		});
	};

	var getThreatsBySpeciesId = function(species,range) {
		setTimeout(function() {
			httpGet('http://apiv3.iucnredlist.org/api/v3/threats/species/id/'+species+'?token=9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee',function() {
				var response = JSON.parse(event.target.response);
				if(typeof response.result[0]!=="undefined") {
					speciesThreatsObject[species] = response;
					speciesThreatsArray[species] = response.result;
				}
				asyncCount++;
				if(asyncCount%rateLimit==0) {
					console.log("Got data for "+asyncCount);
				}
				if(asyncCount>=rateLimit){
					printSpeciesThreatArray();
					buildSpeciesThreats(speciesIdArray,range+rateLimit);
					// alert("Im ready");
				}
			});
		},1);
	};

	var printSpeciesThreatObject = function() {
		body.innerHTML = JSON.stringify(speciesThreatsObject);
	}

	var printSpeciesThreatArray = function() {
		body.innerHTML = JSON.stringify(speciesThreatsArray);
	}

	var buildSpeciesThreats = function(speciesIdArray,range) {
		if(range>=speciesIdArray.length) {
			alert("I'm ready");
			return;
		}
		var endIndex = (range+rateLimit) < speciesIdArray.length ? (range+rateLimit) : speciesIdArray.length;
		console.log("Building the threats for "+range+" to "+endIndex);
		asyncCount = 0;
		for (var i = range; i < endIndex; i++) {
			getThreatsBySpeciesId(speciesIdArray[i],range);
		}
	};
	var buildCategorySpecies = function(categoriesArray) {
		categoriesArray = ['EX'];
		for (var i = 0; i < categoriesArray.length; i++) {
			getSpeciesIdByCategory(categoriesArray[i]);
		}
	};
	return {
		speciesThreatsArray: speciesThreatsArray,
		speciesThreatsObject: speciesThreatsObject,
		buildCategorySpecies: buildCategorySpecies,
		categorySpeciesArray: categorySpeciesArray
	}
})();

// demo - 9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee
// ours - 4dacd864b687de3a777868c1fd2e95071f2c6ac0629ff6018ca1b29b4a2bd90a