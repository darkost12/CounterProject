const TransactCall = artifacts.require("./TransactCall.sol");

module.exports = function(deployer) {
  deployer.deploy(TransactCall);
};
