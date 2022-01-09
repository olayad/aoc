

import fetch from 'node-fetch';
// const fetch = require('node-fetch')

let url='https://adventofcode.com/2021/day/1/input'
let cookie="session=53616c7465645f5f4de5a038aca9ce4b22a5552e1858981bc52ae2dd6ffbf026eac950be83e5270ff909e70e5b0e6f2b"

// fetch(url, {
// 	headers: {
// 		Cookie: cookie
// 	}
// }).then(response => response.json())
// .then(data => console.log(JSON.stringify(data, null, 2)))
const opts = {
	headers: {
		cookie: "session=53616c7465645f5f4de5a038aca9ce4b22a5552e1858981bc52ae2dd6ffbf026eac950be83e5270ff909e70e5b0e6f2b"
	}
};
const result = await fetch(url, opts)
console.log(result)