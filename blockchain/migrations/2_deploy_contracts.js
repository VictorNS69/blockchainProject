const SocialNetwork = artifacts.require("./SocialNetwork.sol")
const fs = require("fs")

module.exports = function(deployer) {
    deployer.deploy(SocialNetwork)
    .then(()=> {
        const file_path = "build/contracts/SocialNetwork-address"
        fs.writeFileSync(file_path, SocialNetwork.address, function (err){
            if (err) throw err
            console.log("Address saved in", file_path)
        })
    })
}