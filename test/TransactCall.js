const {expectEvent} = require('@openzeppelin/test-helpers');
const Web3 = require('web3');
const web3 = new Web3("HTTP://127.0.0.1:8545")
const TransactCall = artifacts.require('TransactCall');
let accounts = web3.eth.getAccounts();


contract('TransactCall', accounts => {

    it ('should be 0 initially', async () => {
        let count = await (await TransactCall.deployed()).getCount();
        assert.equal(
            count.toNumber(),
            0,
            "Initiated with not zero"
        );
    });

    it ('should be possible to set counter', async () => {
        let instance = await TransactCall.deployed();
        await instance.setCount(25);
        assert.equal(
            (await instance.getCount()).toNumber(),
            25,
            "Didn't set to correct number"
        );
    });

    it ('should be possible to increment', async () => {
        let instance = await TransactCall.deployed();
        await instance.setCount(485);
        await instance.increment();
        assert.equal(
            (await instance.getCount()).toNumber(),
            486,
            "Wasn't raised by one"
        );
    });

    it ('should be possible to decrement', async () => {
        let instance = await TransactCall.deployed();
        await instance.setCount(1024);
        await instance.decrement();
        assert.equal(
            (await instance.getCount()).toNumber(),
            1023,
            "Wasn't declined by one"
        );
    });

     it ('should be prohibited to set negative counter', async () => {
        let instance = await TransactCall.deployed();
        await expectEvent(
            await instance.setCount(-3), "FailedSet"
        );
    });

    it ('should be prohibited to decrement when 0', async () => {
        let instance = await TransactCall.deployed();
        await instance.setCount(0);
        await expectEvent(
            await instance.decrement(), "FailedDecrement"
        );
    });

});
