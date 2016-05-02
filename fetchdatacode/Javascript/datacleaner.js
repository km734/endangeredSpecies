var dataCleaner = (function() {

	var body = document.body;

	/* Global datasets */
	var speciesThreats = {};
	var cleanedSpeciesThreats = {};

	var cleanCategory = function(category) {
		httpGet('http://localhost/assignments/project1/project1/speciesThreats3.json',function() {
			speciesThreats = JSON.parse(event.target.response);
			console.log(speciesThreats);
			clean(speciesThreats);
		});
	}

	var clean = function(obj) {
		for(var category in obj) {
			console.log("Processing "+category);
			cleanedSpeciesThreats[category] = {}
			for(var species in obj[category]) {
				var singleCategory = obj[category];
				cleanedSpeciesThreats[category][species] = [];
				for(threat in singleCategory[species]) {
					var code = singleCategory[species][threat]["code"];
					code = parseInt(code);
					if(cleanedSpeciesThreats[category][species].indexOf(code)<0) {
						cleanedSpeciesThreats[category][species].push(code);
					}
				}
			}
		}
		printCleaned();
	}

	var printCleaned = function() {
		console.log("Ready");
		body.innerHTML = JSON.stringify(cleanedSpeciesThreats);
	};


	return {
		speciesThreats: speciesThreats,
		cleanCategory: cleanCategory
	}
})();

// demo - 9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee
// ours - 4dacd864b687de3a777868c1fd2e95071f2c6ac0629ff6018ca1b29b4a2bd90a