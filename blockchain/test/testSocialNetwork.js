const SocialNetwork = artifacts.require("SocialNetwork");
const truffleAssert = require("truffle-assertions");

contract("Test SocialNetwork.sol", async(accounts) => {
    const CLASS_NAME = "SocialNetwork";
    let TEST_ID = 1;

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: adding new user (User1)`, async () => {
        const contract = await SocialNetwork.deployed();

        let users = await contract.getUsers();
        assert.equal(0, users.length);

        const addUser = await contract.addUser("User1");
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == "User1";
        });

        users = await contract.getUsers();
        assert.equal(1, users.length);

        const bytesUser = await contract.getBytes("User1");

        user = await contract.getUser(bytesUser);
        assert.equal("User1", user);
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: adding an existing user (User1)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.addUser("User1"),
            truffleAssert.ErrorType.REVERT,
            "This user is already in the system"
        );

        users = await contract.getUsers();
        assert.equal(1, users.length);
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: sending message to nonexisting user (User2)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.sendMessage("User1", "User2", "hello"),
            truffleAssert.ErrorType.REVERT,
            "The user 2 is not in the system"
        );
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: sending message from nonexisting user (User2)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(1, users.length);

        await truffleAssert.fails(
            contract.sendMessage("User2", "User1", "hello"),
            truffleAssert.ErrorType.REVERT,
            "The user 1 is not in the system"
        );
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: sending message between users (User2)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        const addUser = await contract.addUser("User2");
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == "User2";
        });

        let users = await contract.getUsers();
        assert.equal(2, users.length);
        
        const sendMessage = await contract.sendMessage("User1", "User2", "hello");
        truffleAssert.eventEmitted(sendMessage, "sendMessageEvent", (event) => {
            return event._user1 == "User1" && event._user2 == "User2" && event._message === "hello";
        });
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: removing nonexisting user (User0)`, async () => {
        const contract = await SocialNetwork.deployed();

        await truffleAssert.fails(
            contract.removeUser("User0"),
            truffleAssert.ErrorType.REVERT,
            "This user is not in the system"
        );
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: removing a user in the middle of the array (User2)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        const addUser = await contract.addUser("User3");
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == "User3";
        });

        let users = await contract.getUsers();
        assert.equal(3, users.length);

        const bytesUser = await contract.getBytes("User2");

        let user = await contract.getUser(bytesUser);
        assert.equal("User2", user);

        const delUser = await contract.removeUser("User2");
        truffleAssert.eventEmitted(delUser, "removeUserEvent", (event) => {
            return event._user == "User2";
        });

        users = await contract.getUsers();
        assert.equal(2, users.length);

        user = await contract.getUser(bytesUser);
        assert.equal("", user);
    });

    it(`[${CLASS_NAME}] Test ${TEST_ID++}: removing the last user of the array (User3)`, async () => {
        const contract = await SocialNetwork.deployed();
        
        let users = await contract.getUsers();
        assert.equal(2, users.length);

        const bytesUser = await contract.getBytes("User3");

        let user = await contract.getUser(bytesUser);
        assert.equal("User3", user);

        const delUser = await contract.removeUser("User3");
        truffleAssert.eventEmitted(delUser, "removeUserEvent", (event) => {
            return event._user == "User3";
        });

        users = await contract.getUsers();
        assert.equal(1, users.length);

        user = await contract.getUser(bytesUser);
        assert.equal("", user);
    });
});
