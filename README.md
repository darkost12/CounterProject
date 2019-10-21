# TransactCall
Ethereum smart contract of simple counter
## Installation
```bash
npm run build
yarn build
```
## Only compile
```bash
npm run compile
yarn compile
```
## Tests are available
```bash
npm run test
npm run coverage
```
or
```bash
yarn test
yarn coverage
```
## Python interface application and tests
* IMPORTANT! Before usage and running tests make sure your ganache is on and environment variable CONT_ADDR is set!
```bash
pytest test_counter.py
pytest --cov counter test_counter.py
```
## Linter
```bash
npm run lint
yarn lint
```
* Only .sol
```bash
npm run lint:sol
yarn sol
```
* Only .js
```bash
npm run lint:js
npm run lint:js:fix
yarn lint:js
yarn lint:js:fix
```
