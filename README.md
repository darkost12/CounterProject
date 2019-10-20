# TransactCall
* Ethereum smart contract of simple counter
## Installation
```bash
git clone https://github.com/darkost12/TransactCall
yarn add TransactCall
```
## Tests:
* Before running tests make sure your ganache is on and environment variable CONT_ADDR is set!
```bash
pytest test_TransactCall.py
pytest --cov TransactCall test_TransactCall.py

truffle test
npx solidity-coverage
```
