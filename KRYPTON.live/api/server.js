const errors = require('restify-errors');
const krypton = require('./krypton');

module.exports = function(server) {
	server.get({url: '/query/:type/:address', validation: {
		resources: {
			type: { isRequired: true, isIn: ['uuid','provider','location'] },
			address: { isRequired: true }
		},
	}}, (request, result, next) => {
		const results = krypton.query(request.params.type, request.params.address);
		result.send(request.params);
	});
}
