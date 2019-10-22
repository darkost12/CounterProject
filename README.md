# CounterSolidiy
Ethereum smart contract featuring a simple counter for studying purposes.

## How to use
```bash
# Compile contracts to ./build
npm run build

# Test contracts
npm run test

# Perform code coverage analysis
npm run coverage

# Perform linting (all / only .sol files / only .js files)
npm run lint
npm run lint:sol
npm run lint:js
npm run lint:js:fix
```

## Python CLI application and tests (/app directory)
* IMPORTANT! Before usage and running tests make sure your ganache is running and environment variable CONT_ADDR is set!
Run tests from /app directory!
```bash
pytest test_counter.py
pytest --cov counter test_counter.py
```
