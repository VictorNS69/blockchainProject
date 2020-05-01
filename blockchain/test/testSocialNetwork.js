const SocialNetwork = artifacts.require("SocialNetwork");
const truffleAssert = require("truffle-assertions");

contract("Test SocialNetwork.sol", async(accounts) => {
    const CLASS_NAME = "SocialNetwork";

    it(`[${CLASS_NAME}] Test 1: adding new user`, async () => {
        const contract = await SocialNetwork.deployed();

        let users = await contract.getUsers();
        assert.equal(0, users.length);

        let user = await contract.getUser(1);
        assert.equal(false, user);

        const addUser = await contract.addUser(1);
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == 1;
        });
        users = await contract.getUsers();
        assert.equal(1, users.length);

        user = await contract.getUser(1);
        assert.equal(true, user);
    });

    it(`[${CLASS_NAME}] Test 2: adding a existing user`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.addUser(1),
            truffleAssert.ErrorType.REVERT,
            "This user is already in the system"
        );

        users = await contract.getUsers();
        assert.equal(1, users.length);
    });

    it(`[${CLASS_NAME}] Test 3.1: sending message to an unexisting user (user 2)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.sendMessage(1, 2),
            truffleAssert.ErrorType.REVERT,
            "The user 2 is not in the system"
        );
    });

    it(`[${CLASS_NAME}] Test 3.2: sending message to an unexisting user (user 1)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.sendMessage(2, 1),
            truffleAssert.ErrorType.REVERT,
            "The user 1 is not in the system"
        );
    });

    it(`[${CLASS_NAME}] Test 3: sending message between users`, async () => {
        const contract = await SocialNetwork.deployed();
        
        const addUser = await contract.addUser(2);
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == 2;
        });

        let users = await contract.getUsers();
        assert.equal(2, users.length);
        
        const sendMessage = await contract.sendMessage(1,2);
        truffleAssert.eventEmitted(sendMessage, "sendMessageEvent", (event) => {
            return event._user1 == 1 && event._user2 == 2;
        });
    });

});