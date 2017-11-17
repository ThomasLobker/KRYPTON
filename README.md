# KRYPTON
KRYPTON is a Smart Contract and ecosystem to provide SIP registration on the NEO blockchain using a KRYPTON compatible SIP provider. With KRYPTON you can decentralize SIP trunking and provide real-time payments per call. As a bonus feature NEO users can call and message each other directly on their public address.

- [Background](#background)
- [Scope](#scope)
- [Usage](#usage)
- [License](#license)
- [Development](#development)

## Background
The primary purpose of KRYPTON is to deliver a friendly and secure ecosystem between users and providers of telecom solutions. A user can choose a provider and register on the network. Authorization and payments are done real-time on the NEO blockchain.

#### The problem
Many providers offer telecom solutions for their users on either a postpaid basis with a monthly billing cycle or on a prepaid basis. In order to offer a monthly billing cycle the provider needs to setup an account for the user based on trust. Many users default on their account and providers have to deal with late payments. When using a prepaid solution the user has to maintain their balance and this makes switching providers or withdrawal quite a hassle. More importantly both solutions are based on trust.

#### The solution
KRYPTON is offering a solution where users can have a prepaid wallet, where the funds are staying in full control of the user at any time. Users can switch providers at any time, or even use multiple providers at the same time, using the same prepaid balance. For example if you want to make domestic calls with a different provider than foreign calls.

## Scope

#### Smart Contract
The Smart Contract will provide a trustless bridge between user and provider, using blockchain technology built on the NEO Smart Economy.

- Use a NEO public address as a digital identity
- User authorization
- Registration of users on the network of a provider
- Deploying providers with outbound proxy address
- Reservation and withdrawals of NeoGas during phone calls (_not yet available in version 1_)

[Read more](contract/README.md)

#### User
The user will be provided with a hybrid softphone with built-in crypto currency wallet. The wallet will hold NeoGas as a digital asset and the user has full control over the funds.

- Web-based JavaScript client
- WebSockets for real-time communication
- Open-source

[Read more](user/README.md)

#### Provider
The provider will have access to small set of tools and knowledge to deploy their services on the blockchain.

- Local wallet service for communication with the blockchain
- Python registration script for easy implementation in [Kamailio SIP Proxy](https://www.kamailio.org/)
- Kamailio based WebSocket proxy
- Open-source

[Read more](provider/README.md)

#### Service
The ecosystem will be friendly and accessible using the __KRYPTON.live__ service where providers can sign up and users can search and find the best provider for their needs. An open API will offer a transparent layer between the user and provider to configure and manage the service.

[Read more](KRYPTON.live/README.md)

## Usage
Basic usage of the Smart Contract:
```
invoke SCRIPTHASH function ["parameter","parameter","parameter"]
```
- `SCRIPTHASH` The public hash of the smart contract on the NEO blockchain
- `function` The function to be triggered, with additional parameters
  - __`version []`__ Retrieve the Smart Contract version
  - __`deploy ["provider","hostname"]`__ Deploy the provider on the blockchain
    - `provider` The public NEO address of the provider
    - `location` The (DNS SRV) location of the outbound proxy
  - __`undeploy ["provider"]`__ Undeploy the provider on the blockchain
    - `provider` The public NEO address of the provider
  - __`register ["user","provider","uuid"]`__ Register the user on the blockchain
    - `user` The public NEO address of the user
    - `provider` The public NEO address of the provider
    - `uuid` The (RFC 4122 compliant) version 4 UUID for authorization
  - __`unregister ["user"]`__ Register the user on the blockchain
    - `user` The public NEO address of the user
  - __`query ["type","user"]`__ Query a user on the network
    - `type` Query the user `uuid` or `location`
    - `user` The public NEO address of the user

## License
- KRYPTON is open-source under [MIT license](https://github.com/MediaServe/KRYPTON/LICENSE.md)
- Maintained by [Thomas Lobker](https://www.linkedin.com/in/thomaslobker/)

## Development
Development is currently planned in four phases.

### Phase 1: _Smart Contract_
In this early phase we will deliver the basic but fully functional Smart Contract to start development on the NEO Smart Economy. The Smart Contract will offer proof of concept by invoking the contract manually.

### Phase 2: _User and provider deployment_
After deploying the Smart Contract we will focus on the wallet implementation on the user and provider side. The wallet will offer a smooth experience in invoking the Smart Contract, for both the user and provider. The user wallet will be fully HTML5 web-based and mobile ready. Releasing the software will create a fully working concept including:
- Making voice calls and sending messages directly between registered NEO addresses
- Making voice calls and sending messages to PSTN (land-line) destinations (and pay in NeoGas!)
- Accept incoming phone calls from PSTN (provider compatibility is required)

### Phase 3: _Update_
We want to update the smart contract to fully support time-based escrow functionality in order to do automatic payments and withdrawals.

### Phase 4: _KRYPTON.live_
Finally we will release a public web-service to make the ecosystem complete. The __KRYPTON.live__ service will offer a market place for providers to sell their serivices. Users can configure and manage their registration through the web-service public API.
