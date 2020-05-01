const SocialNetwork = artifacts.require("SocialNetwork");
const truffleAssert = require("truffle-assertions");

contract("Test SocialNetwork.sol", async(accounts) => {
    const CLASS_NAME = "SocialNetwork";

    it(`[${CLASS_NAME}] Test 1: adding new user`, async () => {
        const contract = await SocialNetwork.deployed();
        const addUser = await contract.addUser(1);
        truffleAssert.eventEmitted(addUser, "addUserEvent", (event) => {
            return event._user == 1;
        });
    });

    it(`[${CLASS_NAME}] Test 2: adding a existing user`, async () => {
        const contract = await SocialNetwork.deployed();
        await truffleAssert.fails(
            contract.addUser(1),
            truffleAssert.ErrorType.REVERT,
            "This user is already in the system"
        );
    });
});