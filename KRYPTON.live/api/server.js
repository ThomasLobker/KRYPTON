const errors = require('restify-errors');
const krypton = require('./krypton');

module.exports = function(server) {
	server.get({url: '/query/:type/:address', validation: {
		resources: {
			type: { isRequired: true, isIn: ['uuid','provider','location'] },
			address: { isRequired: true }
		},
	}}, (request, result, next) => {
		var data = krypton.query({ result, next }, request.params.type, request.params.address);
	});
}
