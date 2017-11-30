// Requirements
const config = require('./config');
const node = require('./blockchain');
const util = require('./util');

// Export KRYPTON functions
module.exports = {
	query: (restify, type, address) => {
		console.log('query', type, address);

		// Query the blockchain for the UUID
		node.getStorage(address).then((result) => {
			if (typeof result === "string") {
				const uuid = result;
				console.log('uuid', uuid);
				switch (type) {
					case "uuid":
						restify.result.send({ "status": "success", "type": type, "address": address, "value": uuid });
						return true;
//						return uuid;
					default:
						node.getStorage(uuid, "scriptHash").then((result) => {
							if (typeof result === "string") {
								const provider = result;
								console.log('provider', provider);
								switch (type) {
									case "provider":
										restify.result.send({ "status": "success", "type": type, "address": address, "value": provider });
										return true;
//										return provider;
									case "location":
										node.getStorage(provider).then((result) => {
											if (typeof result === "string") {
												const location = result;
												console.log('location', location);
												restify.result.send({ "status": "success", "type": type, "address": address, "value": location });
												return true;
//												return location;
											} else {
												console.log('location not found');
												return false;
											}
										}).catch(function(error) {
											console.log(error);
											return false;
										});
								}
							} else {
								console.log('provider not found');
								return false;
							}
						}).catch(function(error) {
							console.log(error);
							return false;
						});
				}
			} else {
				console.log('uuid not found');
				return false;
			}
		}).catch(function(error) {
			console.log(error);
			return false;
		});
	}
}
