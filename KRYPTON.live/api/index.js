// Configuration
const config = require('./config')

// Require NEO components
const neon = require('@cityofzion/neon-js');
const Neon = neon.default;
const node = require('./blockchain')

// Require Restify
const restify = require('restify');
const errors = require('restify-errors');
const validation = require('node-restify-validation');

// Create a NEON account
const account = Neon.create.account(config.wif)

// Create a server
const server = restify.createServer({
	name: config.name,
	version: config.version,
});

// Configure the server
server.use(restify.plugins.jsonBodyParser({ mapParams: false }));
server.use(restify.plugins.acceptParser(server.acceptable));
server.use(restify.plugins.queryParser({ mapParams: true }));
server.use(restify.plugins.fullResponse());
server.use(validation.validationPlugin({
	errorsAsArray: false,
	forbidUndefinedVariables: false,
	errorHandler: errors.InvalidArgumentError
}));

// Start the server and listen for requests
server.listen(config.port, function() {
	require('./server')(server);
	console.log(config.name, config.version, 'listening', config.port);
});
