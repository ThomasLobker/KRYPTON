// Requirements
const config = require('./config');
const node = require('./blockchain');
const util = require('./util');

// Export KRYPTON functions
module.exports = {
	query: (restify, type, address) => {
		console.log('query', type, address);

		if (node.isAddress(address)) {
			// Query the blockchain for the UUID
			node.getStorage(address).then((result) => {
				if (typeof result === "string") {
					const uuid = result;
					console.log('uuid', uuid);
					switch (type) {
						case "uuid":
							restify.result.send({ "status": "success", "type": type, "address": address, "code": 200, "value": uuid });
							return true;
						default:
							node.getStorage(uuid, "scriptHash").then((result) => {
								if (typeof result === "string") {
									const provider = result;
									console.log('provider', provider);
									switch (type) {
										case "provider":
											restify.result.send({ "status": "success", "type": type, "address": address, "code": 200, "value": provider });
											return true;
										case "location":
											node.getStorage(provider).then((result) => {
												if (typeof result === "string") {
													const location = result;
													console.log('location', location);
													restify.result.send({ "status": "success", "type": type, "address": address, "code": 200, "value": location });
													return true;
												} else {
													console.log('location not found');
													restify.result.send({ "status": "failed", "type": type, "address": address, "code": 404, "message": "Not Found" });
													return false;
												}
											}).catch(function(error) {
												console.log(error);
												restify.result.send({ "status": "failed", "type": type, "address": address, "code": 500, "message": "Internal Server Error" });
												return false;
											});
									}
								} else {
									console.log('provider not found');
									restify.result.send({ "status": "failed", "type": type, "address": address, "code": 404, "message": "Not Found" });
									return false;
								}
							}).catch(function(error) {
								console.log(error);
								restify.result.send({ "status": "failed", "type": type, "address": address, "code": 500, "message": "Internal Server Error" });
								return false;
							});
					}
				} else {
					console.log('uuid not found');
					restify.result.send({ "status": "failed", "type": type, "address": address, "code": 404, "message": "Not Found" });
					return false;
				}
			}).catch(function(error) {
				console.log(error);
				restify.result.send({ "status": "failed", "type": type, "address": address, "code": 500, "message": "Internal Server Error" });
				return false;
			});
		} else {
			console.log("invalid NEO address");
			restify.result.send({ "status": "failed", "type": type, "address": address, "code": 503, "message": "Invalid Address" });
			return false;
		}
	}
}
