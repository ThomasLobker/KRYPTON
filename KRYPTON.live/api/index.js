// Require NEO components
const neon = require('@cityofzion/neon-js');
const Neon = neon.default;
const node = require('./blockchain')
const config = require('./config')
const account = Neon.create.account(config.wif)

