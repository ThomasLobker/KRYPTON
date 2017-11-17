# KRYPTON
# https://krypton.live/

# Version: 1 (2017-11-16)
# Author: Thomas Lobker
# Copyright: MediaServe International
# License: MIT

# KRYPTON is a Smart Contract to provide SIP registration on the NEO blockchain
# using a KRYPTON compatible SIP provider. With KRYPTON you can decentralize
# SIP trunking and provide real-time payments per call.

from boa.blockchain.vm.Neo.Runtime import Log, Notify, GetTrigger, CheckWitness
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat

# Script hash of the KRYPTON provider wallet
KRYPTON = b'\x0b\xf5\xe0J\xffj\x97\x03\\\xdeH\x98i\x86\xf4\xe3\xfa`\x9fy'
VERSION = 1

def Main(operation, args):
    """
    Main definition for the KRYPTON smart contact

    :param operation: the operation to be performed
    :type operation: str

    :param args: an optional list of arguments
    :type args: list

    :return: indicating the successful execution of the smart contract
    :rtype: bool
    """

    trigger = GetTrigger()

    if trigger == Verification():
        is_owner = CheckWitness(KRYPTON)

        if is_owner:
            return True

        return False

    elif trigger == Application():
        # Check the version for compatability
        if operation == 'version':
            version = VERSION
            Notify(version)
            return version

        # Let the provider deploy on the blockchain
        elif operation == 'deploy':
            if (len(args) == 2):
                # Read arguments
                provider = args[0]
                location = args[1]

                # Deploy the provider
                Log('FUNC_DEPLOY')
                deploy = Deploy(provider, location)
                return deploy

            else:
                Log('INVALID_ARGUMENTS')
                return False

        # Let the provider undeploy on the blockchain
        elif operation == 'undeploy':
            if (len(args) == 1):
                # Read arguments
                provider = args[0]

                # Undeploy the provider
                Log('FUNC_UNDEPLOY')
                undeploy = Undeploy(provider)
                return undeploy

            else:
                Log('INVALID_ARGUMENTS')
                return False

        # Let the user register to a provider
        elif operation == 'register':
            if (len(args) == 3):
                # Read arguments
                user = args[0]
                provider = args[1]
                uuid = args[2]

                # Register the user
                Log('FUNC_REGISTER')
                register = Register(user, provider, uuid)
                return register

            else:
                Log('INVALID_ARGUMENTS')
                return False

        # Let the user unregister to a provider
        elif operation == 'unregister':
            if (len(args) == 1):
                user = args[0]

                # Unregister the user
                Log('FUNC_UNREGISTER')
                unregister = Unregister(user)
                return unregister

            else:
                Log('INVALID_ARGUMENTS')
                return False

        # Query a user for UUID or provider
        elif operation == 'query':
            if (len(args) == 2):
                # Read arguments
                query = args[0]
                user = args[1]

                # Query the user for UUID or provider
                Log('FUNC_QUERY')
                queryuser = QueryUser(query, user)
                return queryuser

            else:
                Log('INVALID_ARGUMENTS')
                return False

        Log('INVALID_FUNCTION')
        return False

    Log('FORBIDDEN')
    return False

def Deploy(provider, location):
    """
    Deploy a new SIP provider to the KRYPTON network

    :param provider: the address of the SIP provider wallet
    :type provider: str

    :param location: the (DNS SRV) location of the outbound proxy
    :type location: str

    :return: whether the deploy was successful
    :rtype: bool
    """

    if not CheckWitness(provider):
        Log('FORBIDDEN')
        return False

    context = GetContext()
    address = Get(context, provider)

    # Deploy the provider
    if (address == 0):
        Put(context, provider, location)
        Log('DEPLOY_SUCCESS')
        return True

    Log('DEPLOY_FAILED')
    return False

def Undeploy(provider):
    """
    Undeploy a provider from the KRYPTON network

    :param provider: the address of the SIP provider wallet
    :type provider: str

    :return: whether the deploy was successful
    :rtype: bool
    """

    if not CheckWitness(provider):
        Log('FORBIDDEN')
        return False

    context = GetContext()
    address = Get(context, provider)

    # Remove deployment
    if not (address == 0):
        Delete(context, provider)
        Log('UNDEPLOY_SUCCESS')
        return True

    # No deployment found
    Log('UNDEPLOY_FAILED')
    return False

def Register(user, provider, uuid):
    """
    Register a user with a provider and use the provided UUID as
    authorization nonce

    :param user: the public address of the user
    :type user: str

    :param provider: the public address of the provider
    :type provider: str

    :param uuid: the UUID supplied by provider and confirmed by user
    :type uuid: str

    :return: whether the registration was successful
    :rtype: bool
    """

    # Check if the UUID format is validating
    if not (CheckUUID(uuid)):
        return False

    # Check if the user is validating the transaction
    if not CheckWitness(user):
        Log('FORBIDDEN')
        return False

    context = GetContext()
    address = Get(context, provider)

    # Check if provider exists
    if (address == 0):
        Log('PROVIDER_ABSENT')
        return False

    address = Get(context, user)

    # Remove old registration before inserting new registration
    if not (address == 0):
        Delete(context, user)
        Delete(context, uuid)
        Log('UNREGISTER_SUCCESS')

    # Store new registration
    Put(context, user, uuid)
    Put(context, uuid, provider)
    Log('REGISTER_SUCCESS')
    return True

def Unregister(user):
    """
    Unregister a user from the KRYPTON network

    :param user: the public address of the user
    :type user: str

    :return: whether the registration was successful
    :rtype: bool
    """

    # Check if the user is validating the transaction
    if not CheckWitness(user):
        Log('FORBIDDEN')
        return False

    context = GetContext()
    uuid = Get(context, user)

    if not (uuid == 0):
        # Remove registration
        Delete(context, user)
        Delete(context, uuid)
        Log('UNREGISTER_SUCCESS')
        return True

    # No registration found
    Log('UNREGISTER_FAILED')
    return False

def QueryUser(query, user):
    """
    Query a user on the KRYPTON network

    :param query: type of query is UUID or provider
    :type query: str

    :param user: the public address of the user
    :type user: str

    :return: whether the query was successful
    :rtype: bool
    """

    context = GetContext()

    uuid = Get(context, user)

    if (uuid == 0):
        Log('QUERY_USER_FAILED')
        return False

    if (query == "uuid"):
        Notify(uuid)
        return True

    provider = Get(context, uuid)

    if (provider == 0):
        Log('QUERY_PROVIDER_FAILED')
        return False

    if (query == "provider"):
        Notify(provider)
        return True

    location = Get(context, provider)

    if (location == 0):
        Log('QUERY_LOCATION_FAILED')
        return False

    if (query == "location"):
        Notify(location)
        return True

    # User or data not found
    Log('QUERY_FAILED')
    return False

def CheckUUID(uuid):
    """
    Check a UUID to see if the format is valid

    :param entity: the UUID to check
    :type entity: str

    :return: whether the check was successful
    :rtype: bool
    """

    Log("CHECK_UUID_LEN")
    if (len(uuid) != 36):
        Log('UUID_INVALID_LEN')
        return False

    Log("CHECK_UUID_DASH")
    dashes = [8, 13, 18, 23]
    for dash in dashes:
        if not (uuid[dash:dash+1] == '-'):
            Log('UUID_INVALID_DASH')
            return False

    Log("CHECK_UUID_VERSION")
    if not (uuid[14:15] == '4'):
        Log('UUID_INVALID_VERSION')
        return False

    Log('UUID_VALID')
    return True
