const { expectEvent } = require('@openzeppelin/test-helpers');
const Counter = artifacts.require('Counter');

contract('Counter', function ([sender]) {
  it('should be 0 initially', async () => {
    const count = await (await Counter.deployed()).getCount();
    assert.equal(
      count.toNumber(),
      0,
      'Initiated with not zero'
    );
  });

  it('should be possible to set counter', async () => {
    const instance = await Counter.deployed();
    await instance.setCount(25);
    assert.equal(
      (await instance.getCount()).toNumber(),
      25,
      'Didn\'t set to correct number'
    );
  });

  it('should be possible to increment', async () => {
    const instance = await Counter.deployed();
    await instance.setCount(485);
    await instance.increment();
    assert.equal(
      (await instance.getCount()).toNumber(),
      486,
      'Wasn\'t incremented'
    );
  });

  it('should be possible to decrement', async () => {
    const instance = await Counter.deployed();
    await instance.setCount(1024);
    await instance.decrement();
    assert.equal(
      (await instance.getCount()).toNumber(),
      1023,
      'Wasn\'t decremented'
    );
  });

  it('should be prohibited to set negative counter', async () => {
    const instance = await Counter.deployed();
    await expectEvent(
      await instance.setCount(-3), 'FailedSet'
    );
  });

  it('should be prohibited to decrement when 0', async () => {
    const instance = await Counter.deployed();
    await instance.setCount(0);
    await expectEvent(
      await instance.decrement(), 'FailedDecrement'
    );
  });
});
