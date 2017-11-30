# KRYPTON
KRYPTON is a Smart Contract and ecosystem to provide SIP registration on the NEO blockchain using a KRYPTON compatible SIP provider. With KRYPTON you can decentralize SIP trunking and provide real-time payments per call. As a bonus feature NEO users can call and message each other directly on their public address.

[Return](../README.md)

## KRYPTON.live public web-service
The public web-service will provide as a marketplace where users and providers will connect. We are still in a very early stage of developing the web-service.

## API
The API provides a REST API to query the KRYPTON.live smart contract back-end.

### Installation
Designed to be working in the following environment:
- Ubuntu Linux `16.04 LTS`
- NodeJS `8.9.1`
- NPM `5.5.1`

```
git clone https://github.com/MediaServe/KRYPTON.git
cd KRYPTON/KRYPTON.live/api/
npm install
cp config.js.example config.js
nodejs index.js
```

The API is designed to run in the background, you may use `GNU Screen` for example, behind a HTTP proxy like Apache2 or nginx.

### Usage
Query the API to get real-time information from the smart contract storage back-end.

Basic usage of the API (_result is a JSON object_):
```
https://krypton.live/api/query/TYPE/USER
```
- `query` The function to be triggered, with additional parameters
  - __`query/TYPE/USER`__ Query a user on the network
    - `type` Query the user `uuid`, `location` or `provider` value
    - `user` The public NEO address of the user

More functions will be added in a later stage.
