# KRYPTON
KRYPTON is a Smart Contract and ecosystem to provide SIP registration on the NEO blockchain using a KRYPTON compatible SIP provider. With KRYPTON you can decentralize SIP trunking and provide real-time payments per call. As a bonus feature NEO users can call and message each other directly on their public address.

## Smart Contract
The smart contract is the heart of the KRYPTON network. We chose for the fast and highly scalable NEO blockchain.

### Examples
Check the version of the deployed smart contract
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 version []
```

Deploy a new provider with public NEO address `ATRETdhRTg9AWT6s4DhJfTtCDNPxgfuPxk` and hostname `proxy.krypton.live`
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 deploy ["ATRETdhRTg9AWT6s4DhJfTtCDNPxgfuPxk","proxy.krypton.live"]
```

Register a new user with public address `AGs7dP8tX1KgjXopLELdmZed85GnEkFPRh` on provider `ATRETdhRTg9AWT6s4DhJfTtCDNPxgfuPxk` with UUID `05661611-4074-4b52-a1e2-8d47cd43bd02`
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 register ["AGs7dP8tX1KgjXopLELdmZed85GnEkFPRh","ATRETdhRTg9AWT6s4DhJfTtCDNPxgfuPxk","05661611-4074-4b52-a1e2-8d47cd43bd02"]
```

Query the user and get the UUID and location where to find him
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 query ["uuid","AGs7dP8tX1KgjXopLELdmZed85GnEkFPRh"]
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 query ["location","AGs7dP8tX1KgjXopLELdmZed85GnEkFPRh"]
```

Unregister the user from the network
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 unregister ["AGs7dP8tX1KgjXopLELdmZed85GnEkFPRh"]
```

Undeploy the provider from the network
```
testinvoke c7faa6f0e14f3b355a23b69b0689c45c17ea5a78 undeploy ["ATRETdhRTg9AWT6s4DhJfTtCDNPxgfuPxk"]
```

[Return](../README.md)
